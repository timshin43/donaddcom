# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-18 02:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('anim_site_main', '0004_auto_20180902_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='single_page',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 18, 2, 50, 54, 998862, tzinfo=utc)),
        ),
    ]
