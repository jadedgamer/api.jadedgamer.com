# Generated by Django 2.1.3 on 2018-11-24 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coreExtend', '0001_initial'),
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('slug', models.SlugField(blank=True, max_length=500)),
                ('site_url', models.URLField(blank=True, max_length=500, unique=True)),
                ('feed_url', models.URLField(max_length=500, unique=True)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('feed_type', models.SmallIntegerField(choices=[(1, 'RSS'), (2, 'JSON'), (3, 'Twitter')], default=1)),
                ('approval_status', models.SmallIntegerField(choices=[(1, 'Pending'), (2, 'Denied'), (3, 'Approved')], default=1)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('next_scheduled_update', models.DateTimeField(blank=True, null=True)),
                ('last_story_date', models.DateTimeField(blank=True, null=True)),
                ('num_subscribers', models.IntegerField(default=-1)),
                ('has_feed_exception', models.BooleanField(db_index=True, default=False)),
                ('has_page_exception', models.BooleanField(db_index=True, default=False)),
                ('favicon_color', models.CharField(blank=True, max_length=6, null=True)),
                ('favicon_not_found', models.BooleanField(default=False)),
                ('search_indexed', models.NullBooleanField(default=None)),
                ('pubsub_enabled', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='FeedItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('guid', models.CharField(db_index=True, max_length=500, unique=True)),
                ('title', models.CharField(max_length=500)),
                ('original_title', models.CharField(max_length=500)),
                ('link', models.URLField(max_length=500)),
                ('description', models.TextField(blank=True)),
                ('summary', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('feed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregator.Feed')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='coreExtend.UUIDTaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
        migrations.CreateModel(
            name='FeedList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('can_self_add', models.BooleanField(choices=[(True, 'Only me'), (False, 'Everyone')], default=True, help_text='Who can edit this list?')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='When list was added to the site')),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('feeds', models.ManyToManyField(blank=True, to='aggregator.Feed')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
        migrations.AddField(
            model_name='feed',
            name='feed_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feed_lists', to='aggregator.FeedList'),
        ),
        migrations.AddField(
            model_name='feed',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feeds', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feed',
            name='subscribers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feed',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
