# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-24 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0021_auto_20180123_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicesindexblock',
            name='additional_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='additional_title'),
        ),
        migrations.AddField(
            model_name='servicesindexblock',
            name='consulting_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='consulting_title'),
        ),
        migrations.AddField(
            model_name='servicesindexblock',
            name='monitoring_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='monitoring_title'),
        ),
        migrations.AddField(
            model_name='servicesindexblock',
            name='project_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='project_title'),
        ),
    ]
