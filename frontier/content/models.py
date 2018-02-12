# from django.db import models
from feincms.module.page.models import Page
from django.utils.translation import ugettext_lazy as _
from feincms.content.application.models import ApplicationContent
from .content_types import NewsIndexBlock, ServicesIndexBlock, ConceptIndexBlock, IndexMapBlock, ParthnersBlock, CustomersBlock, ReferencesBlock, ContactsBlock

# Create your models here.

Page.register_extensions(
    'feincms.extensions.changedate',
    'feincms.extensions.translations',
    'feincms.module.page.extensions.navigation',
    'feincms.module.page.extensions.navigationgroups',
    'feincms.extensions.seo',
    'feincms.module.page.extensions.titles'
)  # Example set of extensions


Page.register_templates({
    'title': _('Page'),
    'path': 'content/pages/page.html',
    'regions': (
        ('main', _('Main content area')),
    ),
})

Page.register_templates({
    'title': _('Index Page'),
    'path': 'content/pages/index_page.html',
    'regions': (
        ('main', _('Main content area')),
    ),
})



Page.create_content_type(NewsIndexBlock)
Page.create_content_type(ServicesIndexBlock)
Page.create_content_type(ConceptIndexBlock)
Page.create_content_type(IndexMapBlock)
Page.create_content_type(ParthnersBlock)
Page.create_content_type(CustomersBlock)
Page.create_content_type(ReferencesBlock)
Page.create_content_type(ContactsBlock)

Page.create_content_type(ApplicationContent, APPLICATIONS=(
     ('news.urls', 'News application'),
    # ('cases.urls', 'Cases category'),
))
