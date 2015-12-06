# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20151109_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='wechat_number',
            field=models.CharField(max_length=15, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='zipcode',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
