# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-26 04:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190325_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 4, 35, 42, 840257, tzinfo=utc)),
        ),
    ]
