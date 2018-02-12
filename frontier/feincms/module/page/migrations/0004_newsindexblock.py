# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-20 15:15
from __future__ import unicode_literals

import common.content_types
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20180120_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsIndexBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0, verbose_name='ordering')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newsindexblock_set', to='page.Page')),
            ],
            options={
                'ordering': ['ordering'],
                'abstract': False,
                'verbose_name_plural': 'NewsIndexBlock',
                'db_table': 'page_page_newsindexblock',
                'verbose_name': 'NewsIndexBlock',
                'permissions': [],
            },
            bases=(common.content_types.RenderCTMixin, models.Model),
        ),
    ]