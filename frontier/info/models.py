from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from cloudinary.models import CloudinaryField
from redactor.fields import RedactorField
from django.utils.translation import ugettext_lazy as _
from feincms.apps import app_reverse
from common.utils import get_cloudinary_thumb
from django.utils.dateformat import DateFormat
from django.core.validators import RegexValidator, URLValidator
from sorl.thumbnail import get_thumbnail


@python_2_unicode_compatible
class Info(models.Model):

    adress_footer = models.CharField(blank=False, null=False, max_length=255, verbose_name=_('adress'))
    email_footer = models.CharField(blank=False, null=False, max_length=255, verbose_name=_('email'))
    phone_footer = models.CharField(blank=False, null=False, max_length=255, verbose_name=_('phone_footer'))

    index_top_image = models.ImageField(blank=False, null=False,)
    index_top_title = models.CharField(blank=False, null=False, max_length=255, verbose_name=_('index_top_title'))
    index_top_subtitle = models.CharField(blank=False, null=False, max_length=255, verbose_name=_('index_top_subtitle'))

    logo_header = models.FileField(blank=False, null=False,)

    logo_footer = models.FileField(blank=False, null=False,)
    copyright_text = models.CharField(blank=False, null=False, max_length=255, verbose_name=_('copyright_text'))
    news_top_title = models.CharField(blank=False, null=False, max_length=255, verbose_name=_('news_top_title'))
    news_page_top_image = models.ImageField(blank=False, null=False,)

    def get_news_page_top_image(self):
        return get_thumbnail(self.news_page_top_image,'1280x720', quality=99).url

    def get_index_top_image(self):
        return get_thumbnail(self.index_top_image,'1280x720', quality=99).url


    def __str__(self):
        return "Site information"

    class Meta:
        verbose_name = _('Info')
        verbose_name_plural = _('Info')
        ordering = ['adress_footer',]


class Contact(models.Model):

    image = models.ImageField(blank=False, null=False,)


    name = models.CharField(max_length=200, blank=False)

    position = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('position'))
    phone_number = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('phone_number'))
    email = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('email'))
    in_link = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('in_link'))
    in_profile_name = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('in_profile_link'))

    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def get_image(self):
        return get_thumbnail(self.image,'200x250', quality=99).url
    def get_image_x2(self):
        return get_thumbnail(self.image,'400x500', quality=99).url
    def get_image_x3(self):
        return get_thumbnail(self.image,'600x750', quality=99).url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
        ordering = ('order',)


@python_2_unicode_compatible
class ParthnerLogo(models.Model):

    title = models.CharField(max_length=200, blank=False)

    link = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('link'))

    image = models.ImageField(blank=False, null=False,)

    def __str__(self):
        return self.title

    def get_image(self):
        #return self.image.url 
        return get_thumbnail(self.image,'200x250', quality=99).url

    def get_image_x2(self):
        return get_thumbnail(self.image,'400x500', quality=99).url

    def get_image_x3(self):
        return get_thumbnail(self.image,'600x750', quality=99).url

    class Meta:
        verbose_name = _('ParthnerLogo')
        verbose_name_plural = _('ParthnerLogo')

@python_2_unicode_compatible
class MenuLinks(models.Model):

    news_block_title = models.CharField(max_length=200, blank=True)

    services_block_title = models.CharField(max_length=200, blank=True)

    concept_block_title = models.CharField(max_length=200, blank=True)

    references_block_title = models.CharField(max_length=200, blank=True)

    contacts_block_title = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "MenuLinks"

    class Meta:
        verbose_name = _('MenuLinks')
        verbose_name_plural = _('MenuLinks')
