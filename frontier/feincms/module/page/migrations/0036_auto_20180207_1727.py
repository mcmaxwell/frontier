# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-02-07 17:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0035_parthnersblock_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parthnersblock',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='referencesblock',
            name='logo',
        ),
    ]
