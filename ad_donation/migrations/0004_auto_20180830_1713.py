# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-30 21:13
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ad_donation', '0003_donations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 30, 21, 13, 21, 580732, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='donations',
            name='who_donated',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
