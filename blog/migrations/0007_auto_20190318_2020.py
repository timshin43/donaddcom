# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 03:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190317_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 19, 3, 20, 23, 344945, tzinfo=utc)),
        ),
    ]
