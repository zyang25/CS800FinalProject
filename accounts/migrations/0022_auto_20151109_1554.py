# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20151108_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='name',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(default=1, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(default=1, max_length=35),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='city',
            field=models.CharField(max_length=35, blank=True),
        ),
    ]
