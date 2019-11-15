# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-26 04:15
from __future__ import unicode_literals

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190323_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog_post',
            name='content_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog_post',
            name='name_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='blog_post',
            name='name_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 4, 15, 51, 604069, tzinfo=utc)),
        ),
    ]
