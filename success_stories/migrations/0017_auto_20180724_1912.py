# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-24 23:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('success_stories', '0016_auto_20180724_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='success_stories',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 24, 23, 12, 11, 745967, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tags',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 24, 23, 12, 11, 745967, tzinfo=utc)),
        ),
    ]
