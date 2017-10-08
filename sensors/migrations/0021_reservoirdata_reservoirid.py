# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-07 23:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0020_auto_20171008_0449'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservoirdata',
            name='reservoirid',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='sensors.reservoir'),
            preserve_default=False,
        ),
    ]
