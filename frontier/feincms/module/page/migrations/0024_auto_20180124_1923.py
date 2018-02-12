# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-24 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0023_auto_20180124_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesindexblock',
            name='additional_text',
            field=redactor.fields.RedactorField(blank=True, verbose_name='service_text_two'),
        ),
        migrations.AlterField(
            model_name='servicesindexblock',
            name='additional_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='service_title_two'),
        ),
        migrations.AlterField(
            model_name='servicesindexblock',
            name='consulting_text',
            field=redactor.fields.RedactorField(blank=True, verbose_name='service_text_one'),
        ),
        migrations.AlterField(
            model_name='servicesindexblock',
            name='consulting_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='service_title_one'),
        ),
        migrations.AlterField(
            model_name='servicesindexblock',
            name='monitoring_text',
            field=redactor.fields.RedactorField(blank=True, verbose_name='service_title_three'),
        ),
        migrations.AlterField(
            model_name='servicesindexblock',
            name='monitoring_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='service_title_three'),
        ),
        migrations.AlterField(
            model_name='servicesindexblock',
            name='project_text',
            field=redactor.fields.RedactorField(blank=True, verbose_name='service_title_four'),
        ),
        migrations.AlterField(
            model_name='servicesindexblock',
            name='project_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='service_title_four'),
        ),
    ]