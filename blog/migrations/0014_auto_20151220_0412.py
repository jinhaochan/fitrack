# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 04:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nineku', '0013_auto_20151220_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dreamdb',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 20, 4, 12, 30, 243828)),
        ),
    ]
