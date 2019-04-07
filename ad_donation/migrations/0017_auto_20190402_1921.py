# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-03 02:21
from __future__ import unicode_literals

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ad_donation', '0016_auto_20190325_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_for_donations',
            name='content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project_for_donations',
            name='content_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project_for_donations',
            name='name_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='project_for_donations',
            name='name_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='project_for_donations',
            name='short_description_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='project_for_donations',
            name='short_description_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='donations',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 3, 2, 21, 41, 45334, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project_for_donations',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 3, 2, 21, 41, 35334, tzinfo=utc)),
        ),
    ]
