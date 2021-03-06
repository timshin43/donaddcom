# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-03 02:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ad_donation', '0017_auto_20190402_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='company_name',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='video',
            name='language',
            field=models.CharField(default='ru', max_length=50),
        ),
        migrations.AddField(
            model_name='video',
            name='link',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='donations',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 3, 2, 43, 47, 52725, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project_for_donations',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 3, 2, 43, 47, 52725, tzinfo=utc)),
        ),
    ]
