# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 03:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20190318_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='birth_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 19, 3, 49, 59, 33710, tzinfo=utc)),
        ),
    ]
