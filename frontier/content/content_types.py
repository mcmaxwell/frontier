from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from common.content_types import RenderCTMixin
from common.utils import get_cloudinary_thumb
from redactor.fields import RedactorField
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext
from django.template.loader import render_to_string
from sorl.thumbnail import get_thumbnail
from news.models import News
from info.models import Contact, Info, ParthnerLogo
from feincms.admin.item_editor import FeinCMSInline
from sortedm2m.fields import SortedManyToManyField


# @python_2_unicode_compatible
# class ParagraphCT(RenderCTMixin, models.Model):
#     template_name = "content/content_types/text_ct.html"
#     title = models.CharField(blank=False, max_length=255, verbose_name=_('title'))
#     text = RedactorField(
#         verbose_name=_('text'),
#         allow_file_upload=False,
#         allow_image_upload=False,
#         blank=True
#     )

#     def __str__(self):
#         return self.title

#     class Meta:
#         abstract = True
#         verbose_name = _('paragraph')
#         verbose_name_plural = _('paragraphes')

class NewsIndexBlock(RenderCTMixin, models.Model):
	template_name = "content/content_types/news_index_block.html"

	def get_template_data(self):
		first_news = News.objects.all().order_by('-publication_date','-id').first()

		if first_news.image:
			news = News.objects.all().order_by('-publication_date', '-id')[:1]
		else:
			news = News.objects.all().order_by('-publication_date', '-id')[:2]

		return {
			'ctx': self,
			'news': news,
		}

	class Meta:
		abstract = True
		verbose_name = _('NewsIndexBlock')
		verbose_name_plural = _('NewsIndexBlock')

@python_2_unicode_compatible
class ServicesIndexBlock(RenderCTMixin, models.Model):
	template_name = "content/content_types/index_services_block.html"


	title = models.CharField(blank=False, max_length=255, verbose_name=_('title'))

	sub_title = RedactorField(
		verbose_name=_('sub_title'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True
	)

	consulting_image = models.ImageField(blank=True, null=False,)

	consulting_title = models.CharField(blank=True, max_length=255, verbose_name=_('service_title_one'))

	consulting_text = RedactorField(
		verbose_name=_('service_text_one'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True
	)

	additional_image = models.ImageField(blank=True, null=False,)

	additional_title = models.CharField(blank=True, max_length=255, verbose_name=_('service_title_two'))

	additional_text = RedactorField(
		verbose_name=_('service_text_two'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True
	)

	monitoring_image = models.ImageField(blank=True, null=False,)

	monitoring_title = models.CharField(blank=True, max_length=255, verbose_name=_('service_title_three'))

	monitoring_text = RedactorField(
		verbose_name=_('service_title_three'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True
	)

	project_image = models.ImageField(blank=True, null=False,)

	project_title = models.CharField(blank=True, max_length=255, verbose_name=_('service_title_four'))

	project_text = RedactorField(
		verbose_name=_('service_title_four'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True
	)

	def get_consulting_image(self):
		return get_thumbnail(self.consulting_image,'1280x720', quality=99).url

	def get_additional_image(self):
		return get_thumbnail(self.additional_image,'1280x720', quality=99).url

	def get_monitoring_image(self):
		return get_thumbnail(self.monitoring_image,'1280x720', quality=99).url

	def get_project_image(self):
		return get_thumbnail(self.project_image,'1280x720', quality=99).url



	def __str__(self):
		return self.title

	class Meta:
		abstract = True
		verbose_name = _('ServicesIndexBlock')
		verbose_name_plural = _('ServicesIndexBlocks')


@python_2_unicode_compatible
class ConceptIndexBlock(RenderCTMixin, models.Model):
	template_name = "content/content_types/index_concept_block.html"

	title = models.CharField(blank=False, max_length=255, verbose_name=_('title'))

	sub_title = RedactorField(
		verbose_name=_('sub_title'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True
	)

	title_one = models.CharField(blank=True, max_length=255, verbose_name=_('title_one'))

	sub_title_one = models.CharField(blank=True, max_length=255, verbose_name=_('sub_title_one'))

	title_two = models.CharField(blank=True, max_length=255, verbose_name=_('title_two'))

	sub_title_two = models.CharField(blank=True, max_length=255, verbose_name=_('sub_title_two'))

	title_three = models.CharField(blank=True, max_length=255, verbose_name=_('title_three'))

	sub_title_three = models.CharField(blank=True, max_length=255, verbose_name=_('sub_title_three'))

	title_four = models.CharField(blank=True, max_length=255, verbose_name=_('title_four'))

	sub_title_four = models.CharField(blank=True, max_length=255, verbose_name=_('sub_title_four'))

	scheme_svg = models.FileField(blank=False, null=False,)

	first_sheme_title =  models.CharField(blank=False, max_length=255, verbose_name=_('first_sheme_title'))

	first_sheme_list = RedactorField(
		verbose_name=_('first_sheme_list'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True
	)


	second_sheme_title =  models.CharField(blank=False, max_length=255, verbose_name=_('second_sheme_title'))

	second_sheme_list = RedactorField(
		verbose_name=_('second_sheme_list'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True
	)


	def get_scheme_image(self):
		return get_thumbnail(self.scheme_image,'1920x1080', quality=99).url


	def __str__(self):
		return self.title

	class Meta:
		abstract = True
		verbose_name = _('ConceptIndexBlock')
		verbose_name_plural = _('ConceptIndexBlock')


@python_2_unicode_compatible
class IndexMapBlock(RenderCTMixin, models.Model):
	template_name = "content/content_types/index_map_block.html"

	houtspot_headline_one = models.CharField(blank=True, max_length=255, verbose_name=_('houtspot_headline_one'))

	hotspot_one_text = RedactorField(
		_('hotspot_one_text'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True,
		null=True
	)

	houtspot_headline_two = models.CharField(blank=True, max_length=255, verbose_name=_('houtspot_headline_two'))

	hotspot_two_text = RedactorField(
		_('hotspot_two_text'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True,
		null=True
	)

	houtspot_headline_three = models.CharField(blank=True, max_length=255, verbose_name=_('houtspot_headline_three'))

	hotspot_three_text = RedactorField(
		_('hotspot_three_text'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True,
		null=True
	)

	houtspot_headline_four = models.CharField(blank=True, max_length=255, verbose_name=_('houtspot_headline_four'))

	hotspot_four_text = RedactorField(
		_('hotspot_four_text'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True,
		null=True
	)

	houtspot_headline_five = models.CharField(blank=True, max_length=255, verbose_name=_('houtspot_headline_five'))

	hotspot_five_text = RedactorField(
		_('hotspot_five_text'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True,
		null=True
	)


	def get_template_data(self):

		return {
			'ctx': self,
		}

	def __str__(self):
		return self.houtspot_headline_one

	class Meta:
		abstract = True
		verbose_name = _('IndexMapBlock')
		verbose_name_plural = _('IndexMapBlock')



# class LogoCTInlines(FeinCMSInline):
# 	filter_horizontal = ['logo']


@python_2_unicode_compatible
class ParthnersBlock(RenderCTMixin, models.Model):
	template_name = "content/content_types/index_parthners_block.html"

	title = models.CharField(blank=False, max_length=255, verbose_name=_('title'))

	sub_title = RedactorField(
		verbose_name=_('sub_title'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True
	)

	#feincms_item_editor_inline = LogoCTInlines

	logo = SortedManyToManyField(ParthnerLogo)

	def __str__(self):
		return self.title

	class Meta:
		abstract = True
		verbose_name = _('ParthnersBlock')
		verbose_name_plural = _('ParthnersBlock')


@python_2_unicode_compatible
class CustomersBlock(RenderCTMixin, models.Model):
	template_name = "content/content_types/index_customers_block.html"

	title = models.CharField(blank=False, max_length=255, verbose_name=_('title'))

	sub_title = RedactorField(
		verbose_name=_('sub_title'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True
	)

	background_image = models.ImageField(blank=False, null=False,)

	network_text = models.CharField(blank=True, max_length=255, verbose_name=_('network_text'))

	money_text = models.CharField(blank=True, max_length=255, verbose_name=_('money_text'))

	cost_text = models.CharField(blank=True, max_length=255, verbose_name=_('cost_text'))


	analitics_text = models.CharField(blank=True, max_length=255, verbose_name=_('analitics_text'))

	speed_text = models.CharField(blank=True, max_length=255, verbose_name=_('speed_text'))

	cube_text = models.CharField(blank=True, max_length=255, verbose_name=_('cube_text'))


	standart_text = models.CharField(blank=True, max_length=255, verbose_name=_('standart_text'))

	clock_text = models.CharField(blank=True, max_length=255, verbose_name=_('clock_text'))

	responce_text = models.CharField(blank=True, max_length=255, verbose_name=_('responce_text'))

	def get_background_image(self):
		return get_thumbnail(self.background_image,'1280x720', quality=99).url



	def __str__(self):
		return self.title

	class Meta:
		abstract = True
		verbose_name = _('CustomersBlock')
		verbose_name_plural = _('CustomersBlock')


@python_2_unicode_compatible
class ReferencesBlock(RenderCTMixin, models.Model):
	template_name = "content/content_types/index_references_block.html"

	title = models.CharField(blank=False, max_length=255, verbose_name=_('title'))

	sub_title = RedactorField(
		verbose_name=_('sub_title'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True
	)

	logo = SortedManyToManyField(ParthnerLogo)

	#feincms_item_editor_inline = LogoCTInlines

	def __str__(self):
		return self.title

	class Meta:
		abstract = True
		verbose_name = _('ReferencesBlock')
		verbose_name_plural = _('ReferencesBlock')



class ContactsBlock(RenderCTMixin, models.Model):
	template_name = "content/content_types/contacts_index_block.html"

	title = models.CharField(blank=False, max_length=255, verbose_name=_('title'))

	sub_title = RedactorField(
		verbose_name=_('sub_title'),
		allow_file_upload=False,
		allow_image_upload=False,
		blank=True
	)

	def get_template_data(self):
		contacts = Contact.objects.all().order_by('order')

		return {
			'ctx': self,
			'contacts': contacts,
		}

	class Meta:
		abstract = True
		verbose_name = _('ContactsBlock')
		verbose_name_plural = _('ContactsBlock')
