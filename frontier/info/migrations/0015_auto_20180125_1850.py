# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-25 18:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0014_menulinks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menulinks',
            name='customers_block_active',
        ),
        migrations.RemoveField(
            model_name='menulinks',
            name='customers_block_title',
        ),
        migrations.RemoveField(
            model_name='menulinks',
            name='customers_block_title_en',
        ),
        migrations.RemoveField(
            model_name='menulinks',
            name='customers_block_title_no',
        ),
        migrations.RemoveField(
            model_name='menulinks',
            name='map_block_active',
        ),
        migrations.RemoveField(
            model_name='menulinks',
            name='map_block_title',
        ),
        migrations.RemoveField(
            model_name='menulinks',
            name='map_block_title_en',
        ),
        migrations.RemoveField(
            model_name='menulinks',
            name='map_block_title_no',
        ),
        migrations.RemoveField(
            model_name='menulinks',
            name='parthners_block_active',
        ),
        migrations.RemoveField(
            model_name='menulinks',
            name='parthners_block_title',
        ),
        migrations.RemoveField(
            model_name='menulinks',
            name='parthners_block_title_en',
        ),
        migrations.RemoveField(
            model_name='menulinks',
            name='parthners_block_title_no',
        ),
    ]