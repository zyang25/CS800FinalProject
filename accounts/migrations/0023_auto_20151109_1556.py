# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20151109_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='introduction',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone_number',
            field=models.CharField(max_length=15, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='wechat_number',
            field=models.DecimalField(max_digits=15, decimal_places=0, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='zipcode',
            field=models.DecimalField(max_digits=15, decimal_places=0, blank=True),
        ),
    ]
