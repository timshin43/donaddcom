# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-24 02:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('funny_stories', '0024_auto_20190422_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funnystories',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 24, 2, 0, 20, 364079, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='funstortag',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 24, 2, 0, 20, 374079, tzinfo=utc)),
        ),
    ]
