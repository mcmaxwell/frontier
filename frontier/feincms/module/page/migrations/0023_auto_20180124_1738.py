# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-24 17:38
from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0022_auto_20180124_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conceptindexblock',
            name='sub_title',
            field=redactor.fields.RedactorField(blank=True, verbose_name='sub_title'),
        ),
        migrations.AlterField(
            model_name='contactsblock',
            name='sub_title',
            field=redactor.fields.RedactorField(blank=True, verbose_name='sub_title'),
        ),
        migrations.AlterField(
            model_name='customersblock',
            name='sub_title',
            field=redactor.fields.RedactorField(blank=True, verbose_name='sub_title'),
        ),
        migrations.AlterField(
            model_name='parthnersblock',
            name='sub_title',
            field=redactor.fields.RedactorField(blank=True, verbose_name='sub_title'),
        ),
        migrations.AlterField(
            model_name='referencesblock',
            name='sub_title',
            field=redactor.fields.RedactorField(blank=True, verbose_name='sub_title'),
        ),
        migrations.AlterField(
            model_name='servicesindexblock',
            name='sub_title',
            field=redactor.fields.RedactorField(blank=True, verbose_name='sub_title'),
        ),
    ]
