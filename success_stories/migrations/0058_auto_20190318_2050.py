# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 03:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('success_stories', '0057_auto_20190318_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='success_stories',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 19, 3, 49, 58, 893310, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tags',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 19, 3, 49, 58, 893310, tzinfo=utc)),
        ),
    ]
