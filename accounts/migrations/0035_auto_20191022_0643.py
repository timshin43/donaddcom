# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-22 10:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_auto_20191020_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='is_advertiser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='birth_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 22, 10, 42, 58, 146866, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='view_count_expire',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 22, 10, 42, 58, 146714, tzinfo=utc)),
        ),
    ]
