# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-30 23:19
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_appuser_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
