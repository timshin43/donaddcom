# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-01 23:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('success_stories', '0041_auto_20180801_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='success_stories',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 1, 23, 29, 42, 37148, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tags',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 1, 23, 29, 42, 37148, tzinfo=utc)),
        ),
    ]
