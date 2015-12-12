# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_usermessage_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
    ]
