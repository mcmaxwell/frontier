# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-20 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('order',), 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='news',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
