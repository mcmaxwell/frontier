# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-02-07 17:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0033_auto_20180207_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parthnersblock',
            name='logo',
        ),
    ]