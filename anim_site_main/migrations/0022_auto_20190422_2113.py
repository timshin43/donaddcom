# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-23 01:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('anim_site_main', '0021_auto_20190421_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='single_page',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 23, 1, 13, 0, 56718, tzinfo=utc)),
        ),
    ]
