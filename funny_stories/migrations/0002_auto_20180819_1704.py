# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-19 21:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('funny_stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funnystories',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 19, 21, 4, 41, 707469, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='funstortag',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 19, 21, 4, 41, 708469, tzinfo=utc)),
        ),
    ]
