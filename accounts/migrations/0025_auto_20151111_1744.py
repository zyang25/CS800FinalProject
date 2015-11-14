# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20151111_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='user',
            new_name='owner',
        ),
    ]
