# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20151116_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='post_id',
            field=models.ForeignKey(to='postManager.PostBase'),
        ),
    ]
