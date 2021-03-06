# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-20 15:32
from __future__ import unicode_literals

import common.content_types
from django.db import migrations, models
import django.db.models.deletion
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_servicesindexblock'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConceptIndexBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('sub_title', models.CharField(max_length=255, verbose_name='sub_title')),
                ('consulting_text', redactor.fields.RedactorField(blank=True, verbose_name='consulting_text')),
                ('region', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0, verbose_name='ordering')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conceptindexblock_set', to='page.Page')),
            ],
            options={
                'ordering': ['ordering'],
                'abstract': False,
                'verbose_name_plural': 'ConceptIndexBlock',
                'db_table': 'page_page_conceptindexblock',
                'verbose_name': 'ConceptIndexBlock',
                'permissions': [],
            },
            bases=(common.content_types.RenderCTMixin, models.Model),
        ),
    ]
