# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_myuser_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_poster',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_vertified',
            field=models.BooleanField(default=False),
        ),
    ]
