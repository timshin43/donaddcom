# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-26 04:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ad_donation', '0015_auto_20190325_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 4, 35, 42, 830257, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project_for_donations',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 4, 35, 42, 830257, tzinfo=utc)),
        ),
    ]
