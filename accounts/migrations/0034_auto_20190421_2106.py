# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-22 04:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_auto_20190421_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='birth_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 22, 4, 6, 52, 746863, tzinfo=utc)),
        ),
    ]
