# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-15 12:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20191115_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 15, 12, 21, 37, 38801, tzinfo=utc)),
        ),
    ]
