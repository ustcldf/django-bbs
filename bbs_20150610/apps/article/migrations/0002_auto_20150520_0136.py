# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('attachments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0001_initial'),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='attachment',
            field=models.ManyToManyField(to='attachments.Attachment'),
        ),
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe7\x9a\x84\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='articletag',
            name='article',
            field=models.ForeignKey(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0', to='article.Article'),
        ),
        migrations.AddField(
            model_name='articletag',
            name='tag',
            field=models.ForeignKey(to='tag.Tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='attachment',
            field=models.ManyToManyField(to='attachments.Attachment', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='forum',
            field=models.ForeignKey(verbose_name=b'\xe7\x89\x88\xe5\x9d\x97', to='forum.Forum'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='tag.Tag', through='article.ArticleTag'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe7\x9a\x84\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
    ]
