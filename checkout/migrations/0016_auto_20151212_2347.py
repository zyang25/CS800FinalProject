# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0015_auto_20151211_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedetails',
            name='amount_items',
            field=models.IntegerField(null=True),
        ),
    ]
