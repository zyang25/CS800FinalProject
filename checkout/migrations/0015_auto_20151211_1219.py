# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0014_auto_20151210_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedetails',
            name='amount_price',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2),
        ),
    ]
