# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-07 14:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20171006_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plants',
            name='userid',
        ),
        migrations.DeleteModel(
            name='Plants',
        ),
    ]
