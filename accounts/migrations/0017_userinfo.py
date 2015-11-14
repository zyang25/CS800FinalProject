# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20151108_0231'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15, blank=True)),
                ('title', models.CharField(max_length=15, blank=True)),
                ('phone_number', models.DecimalField(max_digits=15, decimal_places=0)),
                ('wechat_number', models.DecimalField(max_digits=15, decimal_places=0)),
                ('introduction', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
