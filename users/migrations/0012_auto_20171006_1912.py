# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-06 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_plants_currentplant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plants',
            name='currentplant',
        ),
        migrations.AddField(
            model_name='users',
            name='currentplant',
            field=models.IntegerField(default=8),
            preserve_default=False,
        ),
    ]
