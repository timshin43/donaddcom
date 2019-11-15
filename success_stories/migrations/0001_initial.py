# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-14 17:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Success_stories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2018, 7, 14, 17, 24, 30, 852798, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2018, 7, 14, 17, 24, 30, 852798, tzinfo=utc))),
                ('success_story', models.ManyToManyField(related_name='tags', to='success_stories.Success_stories')),
            ],
        ),
    ]
