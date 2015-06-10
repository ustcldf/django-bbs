# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attachments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField(null=True, verbose_name=b'\xe9\x97\xae\xe9\xa2\x98\xe8\xa1\xa5\xe5\x85\x85', blank=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe7\x9a\x84\xe6\x97\xb6\xe9\x97\xb4', editable=False, blank=True)),
            ],
            options={
                'verbose_name': '\u56de\u7b54',
                'verbose_name_plural': '\u56de\u7b54',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe7\x9a\x84\xe6\x97\xb6\xe9\x97\xb4', editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('body', models.TextField(null=True, verbose_name=b'\xe9\x97\xae\xe9\xa2\x98\xe8\xa1\xa5\xe5\x85\x85', blank=True)),
                ('kw', jsonfield.fields.JSONField(default=dict)),
                ('last_answer_date', models.DateTimeField(null=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x9a\x84\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('answer_count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '\u95ee\u9898',
                'verbose_name_plural': '\u95ee\u9898',
            },
        ),
        migrations.CreateModel(
            name='QuestionAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attachment', models.ForeignKey(verbose_name=b'\xe9\x97\xae\xe9\xa2\x98', to='attachments.Attachment')),
                ('question', models.ForeignKey(verbose_name=b'\xe9\x97\xae\xe9\xa2\x98', to='question.Question')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe7\x9a\x84\xe6\x97\xb6\xe9\x97\xb4', editable=False, blank=True)),
                ('title', models.CharField(max_length=255)),
                ('qescription', models.TextField(null=True, blank=True)),
                ('old_value', models.TextField(null=True, blank=True)),
                ('new_value', models.TextField(null=True, blank=True)),
                ('question', models.ForeignKey(verbose_name=b'\xe9\x97\xae\xe9\xa2\x98', to='question.Question')),
                ('user', models.ForeignKey(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe7\x9a\x84\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': '\u95ee\u9898\u4fee\u6539\u8bb0\u5f55',
                'verbose_name_plural': '\u95ee\u9898\u4fee\u6539\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='QuestionTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.ForeignKey(verbose_name=b'\xe9\x97\xae\xe9\xa2\x98', to='question.Question')),
                ('tag', models.ForeignKey(to='tag.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='attachment',
            field=models.ManyToManyField(to='attachments.Attachment', through='question.QuestionAttachment'),
        ),
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(to='tag.Tag', through='question.QuestionTag'),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe7\x9a\x84\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(verbose_name=b'\xe9\x97\xae\xe9\xa2\x98', to='question.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe7\x9a\x84\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
    ]
