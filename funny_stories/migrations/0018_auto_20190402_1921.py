# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-03 02:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('funny_stories', '0017_auto_20190325_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funnystories',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 3, 2, 21, 41, 45334, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='funstortag',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 3, 2, 21, 41, 45334, tzinfo=utc)),
        ),
    ]
