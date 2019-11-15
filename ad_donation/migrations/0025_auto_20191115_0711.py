# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-15 12:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ad_donation', '0024_auto_20191115_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 15, 12, 11, 57, 254421, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project_for_donations',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 15, 12, 11, 57, 253253, tzinfo=utc)),
        ),
    ]
