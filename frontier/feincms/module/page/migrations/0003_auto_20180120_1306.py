# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-20 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20180120_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='template_key',
            field=models.CharField(choices=[(b'content/pages/page.html', 'Page'), (b'content/pages/index_page.html', 'Index Page')], default=b'content/pages/page.html', max_length=255, verbose_name='template'),
        ),
    ]
