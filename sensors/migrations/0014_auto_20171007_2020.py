# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-07 14:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0013_auto_20171006_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantsensors',
            name='entryid',
        ),
        migrations.RemoveField(
            model_name='reservoir',
            name='entryid',
        ),
        migrations.DeleteModel(
            name='plantsensors',
        ),
        migrations.DeleteModel(
            name='reservoir',
        ),
        migrations.DeleteModel(
            name='weathersensors',
        ),
    ]
