# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('postManager', '0005_auto_20151212_1735'),
        ('checkout', '0012_auto_20151206_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount_price', models.DecimalField(null=True, max_digits=8, decimal_places=2)),
                ('amount_items', models.IntegerField(null=True)),
                ('post_id', models.ForeignKey(to='postManager.PostBase', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
