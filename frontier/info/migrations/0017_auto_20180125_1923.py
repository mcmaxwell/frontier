# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-25 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0016_auto_20180125_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='copyright_text',
            field=models.CharField(default='', max_length=255, verbose_name='copyright_text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='logo_footer',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
