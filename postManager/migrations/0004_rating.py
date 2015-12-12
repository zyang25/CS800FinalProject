# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postManager', '0003_auto_20151208_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.DecimalField(max_digits=1, decimal_places=1)),
                ('post_id', models.ForeignKey(to='postManager.PostBase', null=True)),
            ],
        ),
    ]
