# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-01 23:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20180801_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 1, 23, 34, 49, 135355, tzinfo=utc), max_length=300),
        ),
    ]
