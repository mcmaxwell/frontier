# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-25 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0026_auto_20180125_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='customersblock',
            name='background_image',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]