# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 03:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('funny_stories', '0008_auto_20190318_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funnystories',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 19, 3, 22, 14, 781557, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='funstortag',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 19, 3, 22, 14, 781557, tzinfo=utc)),
        ),
    ]
