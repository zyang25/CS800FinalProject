# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20151108_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='address',
            field=models.CharField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='city',
            field=models.CharField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='zipcode',
            field=models.DecimalField(default=1, max_digits=15, decimal_places=0),
            preserve_default=False,
        ),
    ]
