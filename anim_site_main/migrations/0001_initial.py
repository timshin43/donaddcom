# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-20 21:51
from __future__ import unicode_literals

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Single_Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2018, 8, 20, 21, 51, 38, 40963, tzinfo=utc))),
            ],
        ),
    ]
