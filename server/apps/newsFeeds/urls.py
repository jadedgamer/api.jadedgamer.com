from __future__ import absolute_import
from django.conf.urls import *
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page

from . import views
from . import feeds

app_name="NewsFeeds"
urlpatterns = [
    url(r'^$', views.Index, name = 'index'),
]
