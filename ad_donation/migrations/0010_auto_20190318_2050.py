# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 03:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ad_donation', '0009_auto_20190318_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='project',
            field=models.ManyToManyField(blank=True, related_name='project_donation', to='ad_donation.Project_for_donations'),
        ),
        migrations.AlterField(
            model_name='donations',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 19, 3, 49, 59, 49310, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project_for_donations',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 19, 3, 49, 59, 49310, tzinfo=utc)),
        ),
    ]
