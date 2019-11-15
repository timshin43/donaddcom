# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-22 19:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('success_stories', '0013_auto_20180722_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='success_stories',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 22, 19, 56, 16, 42337, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='success_stories',
            name='story_image',
            field=models.ImageField(upload_to='uploads/success_stories/'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 22, 19, 56, 16, 42337, tzinfo=utc)),
        ),
    ]
