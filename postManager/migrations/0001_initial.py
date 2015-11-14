# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import postManager.helpers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=63)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MoreImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(default=b'', max_length=30, blank=True)),
                ('moreImgs', models.ImageField(upload_to=postManager.helpers.RandomFileName(b'more_img'))),
            ],
        ),
        migrations.CreateModel(
            name='PostBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=30, blank=True)),
                ('start_time', models.DateTimeField(null=True, blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('date_range', models.CharField(default=b'', max_length=30, blank=True)),
                ('is_expired', models.BooleanField(default=False)),
                ('location', models.CharField(default=b'', max_length=50, blank=True)),
                ('short_description', models.CharField(default=b'', max_length=255, blank=True)),
                ('long_description', models.TextField(default=b'', max_length=2048, blank=True)),
                ('short_image', models.ImageField(upload_to=postManager.helpers.RandomFileName(b'short_img'))),
                ('category_id', models.ForeignKey(to='postManager.Category')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='moreimg',
            name='postBase',
            field=models.ForeignKey(related_name='more_img', default=b'', to='postManager.PostBase'),
        ),
    ]
