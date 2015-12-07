# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_userstripe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstripe',
            name='user',
        ),
        migrations.DeleteModel(
            name='userStripe',
        ),
    ]
