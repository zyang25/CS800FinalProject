# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20151108_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivation',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 2, 28, 0, 452425, tzinfo=utc)),
        ),
    ]
