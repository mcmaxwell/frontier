# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-02-07 17:04
from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0031_auto_20180207_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parthnersblock',
            name='sub_title',
            field=redactor.fields.RedactorField(blank=True, verbose_name='su_title'),
        ),
    ]