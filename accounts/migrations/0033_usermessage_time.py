# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_auto_20151212_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 12, 18, 12, 52, 989508), blank=True),
        ),
    ]
