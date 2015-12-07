# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_auto_20151201_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstripe',
            name='user',
            field=models.OneToOneField(default=True, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
