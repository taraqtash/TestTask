# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 11:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171122_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 22, 11, 44, 43, 359304, tzinfo=utc)),
        ),
    ]
