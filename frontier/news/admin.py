# Register your models here.
from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from modeltranslation.admin import TabbedTranslationAdmin
from django.utils.html import format_html
from redactor.fields import RedactorField
from common.admin import CommonPostAdmin
from django import forms
from .models import News
from .translation import TranslationOptions
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class NewsAdmin(SortableAdminMixin,TabbedTranslationAdmin):
    list_display = ('title_no',)

    sortable = 'order'
    fieldsets = (

        (_('News'), {
           'fields': ('image', 'title','text_preview', 'text', ),
       }),
    
    )


admin.site.register(News, NewsAdmin)
