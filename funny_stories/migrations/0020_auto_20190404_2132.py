# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-05 04:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('funny_stories', '0019_auto_20190402_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funnystories',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 5, 4, 32, 38, 435098, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='funstortag',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 5, 4, 32, 38, 436098, tzinfo=utc)),
        ),
    ]
