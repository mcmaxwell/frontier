# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-20 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import feincms.contrib.fields
import feincms.extensions.base
import feincms.module.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameters', feincms.contrib.fields.JSONField(editable=False, null=True)),
                ('region', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0, verbose_name='ordering')),
                ('urlconf_path', models.CharField(max_length=100, verbose_name='application')),
            ],
            options={
                'ordering': ['ordering'],
                'abstract': False,
                'verbose_name_plural': 'application contents',
                'db_table': 'page_page_applicationcontent',
                'verbose_name': 'application content',
                'permissions': [],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('title', models.CharField(help_text='This title is also used for navigation menu items.', max_length=200, verbose_name='title')),
                ('slug', models.SlugField(help_text='This is used to build the URL for this page', max_length=150, verbose_name='slug')),
                ('in_navigation', models.BooleanField(default=False, verbose_name='in navigation')),
                ('override_url', models.CharField(blank=True, help_text="Override the target URL. Be sure to include slashes at the beginning and at the end if it is a local URL. This affects both the navigation and subpages' URLs.", max_length=255, verbose_name='override URL')),
                ('redirect_to', models.CharField(blank=True, help_text='Target URL for automatic redirects or the primary key of a page.', max_length=255, verbose_name='redirect to')),
                ('_cached_url', models.CharField(blank=True, db_index=True, default='', editable=False, max_length=255, verbose_name='Cached URL')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('creation_date', models.DateTimeField(editable=False, null=True, verbose_name='creation date')),
                ('modification_date', models.DateTimeField(editable=False, null=True, verbose_name='modification date')),
                ('language', models.CharField(choices=[(b'en', 'English'), (b'no', 'Norwegian')], default=b'en', max_length=10, verbose_name='language')),
                ('navigation_extension', models.CharField(blank=True, help_text='Select the module providing subpages for this page if you need to customize the navigation.', max_length=200, null=True, verbose_name='navigation extension')),
                ('navigation_group', models.CharField(blank=True, choices=[('default', 'Default'), ('footer', 'Footer')], db_index=True, default='default', max_length=20, verbose_name='navigation group')),
                ('meta_keywords', models.TextField(blank=True, help_text='Keywords are ignored by most search engines.', verbose_name='meta keywords')),
                ('meta_description', models.TextField(blank=True, help_text='This text is displayed on the search results page. It is however not used for the SEO ranking. Text longer than 140 characters is truncated.', verbose_name='meta description')),
                ('_content_title', models.TextField(blank=True, help_text='The first line is the main title, the following lines are subtitles.', verbose_name='content title')),
                ('_page_title', models.CharField(blank=True, help_text='Page title for browser window. Same as title by default. Must be 69 characters or fewer.', max_length=69, verbose_name='page title')),
                ('template_key', models.CharField(choices=[(b'content/pages/page.html', 'Page')], default=b'content/pages/page.html', max_length=255, verbose_name='template')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='page.Page', verbose_name='Parent')),
                ('translation_of', models.ForeignKey(blank=True, help_text='Leave this empty for entries in the primary language.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='page.Page', verbose_name='translation of')),
            ],
            options={
                'ordering': ['tree_id', 'lft'],
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
            },
            bases=(models.Model, feincms.extensions.base.ExtensionsMixin, feincms.module.mixins.ContentModelMixin),
        ),
        migrations.AddField(
            model_name='applicationcontent',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicationcontent_set', to='page.Page'),
        ),
    ]
