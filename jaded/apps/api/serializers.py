import base64
import re
from rest_framework import serializers
from django.conf import settings
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User

from aggregator.models import FeedList, Feed, FeedItem
from news.models import NewsItem, NewsItemInstance


class FeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedItem
        fields = [
            "id",
            "guid",
            "title",
            "original_title",
            "link",
            "thumbnail_url",
            "description",
            "summary",
            "date_added",
            "date_updated",
        ]


class FeedSerializer(serializers.ModelSerializer):
    items = FeedItemSerializer(many=True, read_only=True)

    class Meta:
        model = Feed
        fields = ["id", "title", "slug", "site_url", "feed_url", "feed_display", "items", "date_added", "date_updated"]


class NewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = ["id", "url", "title", "slug", "note", "user", "date_added", "date_updated", "is_hidden"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )
