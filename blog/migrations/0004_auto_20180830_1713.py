# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-30 21:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180830_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 30, 21, 13, 21, 596332, tzinfo=utc)),
        ),
    ]
