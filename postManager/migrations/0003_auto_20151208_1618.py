# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('postManager', '0002_messageboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageboard',
            name='post_id',
            field=models.ForeignKey(to='postManager.PostBase', null=True),
        ),
        migrations.AlterField(
            model_name='messageboard',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
