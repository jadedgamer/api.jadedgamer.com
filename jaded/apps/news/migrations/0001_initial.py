# Generated by Django 2.1.3 on 2018-11-24 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsItem",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("url", models.URLField(blank=True, max_length=510)),
                ("title", models.CharField(max_length=510)),
                ("slug", models.SlugField(max_length=510, unique_for_date="date_added")),
                ("note", models.TextField(blank=True)),
                ("date_added", models.DateTimeField(auto_now_add=True, verbose_name="When list was added to the site")),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("is_hidden", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="newsItems",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={"db_table": "news_item", "ordering": ("-date_added",),},
        ),
        migrations.CreateModel(
            name="NewsItemInstance",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=510)),
                ("slug", models.SlugField(max_length=510)),
                ("date_added", models.DateTimeField(auto_now_add=True, verbose_name="When list was added to the site")),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("note", models.TextField(blank=True)),
                (
                    "newsitem",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="saved_instances",
                        to="news.NewsItem",
                        verbose_name="News",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="saved_news",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={"db_table": "news_item_instance",},
        ),
    ]
