# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-20 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='index_top_image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='info',
            name='index_top_subtitle',
            field=models.CharField(default='', max_length=255, verbose_name='index_top_subtitle'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='index_top_title',
            field=models.CharField(default='', max_length=255, verbose_name='index_top_title'),
            preserve_default=False,
        ),
    ]