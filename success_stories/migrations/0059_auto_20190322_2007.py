# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-23 03:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('success_stories', '0058_auto_20190318_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='success_stories',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 23, 3, 7, 40, 741704, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tags',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 23, 3, 7, 40, 741704, tzinfo=utc)),
        ),
    ]
