# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-04 19:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20180801_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='birth_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 4, 19, 15, 3, 723285, tzinfo=utc)),
        ),
    ]
