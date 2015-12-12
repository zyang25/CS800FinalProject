# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_usermessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='message',
            field=models.CharField(max_length=50),
        ),
    ]
