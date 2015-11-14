# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20151106_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2015, 11, 6, 15, 42, 0, 351464, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
