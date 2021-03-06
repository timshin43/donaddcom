# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 03:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ad_donation', '0007_auto_20190318_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='project',
            field=models.ManyToManyField(blank=True, related_name='project_video', to='ad_donation.Project_for_donations'),
        ),
        migrations.AlterField(
            model_name='donations',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 19, 3, 22, 14, 765957, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project_for_donations',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 19, 3, 22, 14, 765957, tzinfo=utc)),
        ),
    ]
