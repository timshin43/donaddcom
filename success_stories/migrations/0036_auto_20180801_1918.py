# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-01 23:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('success_stories', '0035_auto_20180801_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='success_stories',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 1, 23, 18, 45, 837769, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tags',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 1, 23, 18, 45, 838769, tzinfo=utc)),
        ),
    ]
