# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-20 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20180120_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='index_top_image',
            field=models.ImageField(default='', upload_to=b''),
            preserve_default=False,
        ),
    ]
