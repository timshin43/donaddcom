# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-20 11:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('funny_stories', '0021_auto_20190425_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funnystories',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 20, 11, 24, 15, 5536, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='funstortag',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 20, 11, 24, 15, 6453, tzinfo=utc)),
        ),
    ]
