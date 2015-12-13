# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('postManager', '0001_initial'),
        ('checkout', '0013_purchasedetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasedetails',
            name='post_id',
        ),
        migrations.AddField(
            model_name='purchasedetails',
            name='post_id',
            field=models.ForeignKey(to='postManager.PostBase', null=True),
        ),
        migrations.RemoveField(
            model_name='purchasedetails',
            name='user',
        ),
        migrations.AddField(
            model_name='purchasedetails',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
