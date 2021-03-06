# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-20 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('title_no', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('text_preview', models.CharField(max_length=255, null=True, verbose_name='text_preview')),
                ('text_preview_en', models.CharField(max_length=255, null=True, verbose_name='text_preview')),
                ('text_preview_no', models.CharField(max_length=255, null=True, verbose_name='text_preview')),
                ('text', redactor.fields.RedactorField(blank=True, null=True, verbose_name='text')),
                ('text_en', redactor.fields.RedactorField(blank=True, null=True, verbose_name='text')),
                ('text_no', redactor.fields.RedactorField(blank=True, null=True, verbose_name='text')),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('date', models.DateField(null=True, verbose_name='date')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
    ]
