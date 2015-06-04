# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe7\x9a\x84\xe6\x97\xb6\xe9\x97\xb4', editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('avatar', models.ImageField(default=b'tag-default.png', upload_to=b'', verbose_name=b'\xe5\x9b\xbe\xe6\xa0\x87')),
                ('describe', models.TextField(null=True, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe7\x9a\x84\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
    ]
