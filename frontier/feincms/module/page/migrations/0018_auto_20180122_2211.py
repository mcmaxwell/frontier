# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-22 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0017_auto_20180122_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='customersblock',
            name='analitics_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='analitics_text'),
        ),
        migrations.AddField(
            model_name='customersblock',
            name='clock_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='clock_text'),
        ),
        migrations.AddField(
            model_name='customersblock',
            name='cost_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='cost_text'),
        ),
        migrations.AddField(
            model_name='customersblock',
            name='cube_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='cube_text'),
        ),
        migrations.AddField(
            model_name='customersblock',
            name='money_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='money_text'),
        ),
        migrations.AddField(
            model_name='customersblock',
            name='network_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='network_text'),
        ),
        migrations.AddField(
            model_name='customersblock',
            name='responce_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='responce_text'),
        ),
        migrations.AddField(
            model_name='customersblock',
            name='speed_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='speed_text'),
        ),
        migrations.AddField(
            model_name='customersblock',
            name='standart_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='standart_text'),
        ),
    ]