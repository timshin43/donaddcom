# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-18 02:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ad_donation', '0005_auto_20180902_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 18, 2, 50, 55, 92462, tzinfo=utc)),
        ),
    ]
