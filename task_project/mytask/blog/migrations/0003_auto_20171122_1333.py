# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 11:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171122_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 22, 11, 33, 42, 721829, tzinfo=utc)),
        ),
    ]
