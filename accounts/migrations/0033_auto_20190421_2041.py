# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-22 03:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_auto_20190404_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='birth_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 22, 3, 41, 32, 169522, tzinfo=utc)),
        ),
    ]
