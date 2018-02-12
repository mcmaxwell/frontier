from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from redactor.fields import RedactorField
from django.utils import translation
from feincms.apps import app_reverse
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
from unidecode import unidecode
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail
from django.utils import timezone



# Create your models here.
@python_2_unicode_compatible
class News(models.Model):

    image = models.ImageField(blank=True, null=True,)

    title = models.CharField(
                max_length=255,
                verbose_name=_('title'),
                null=True,
    )

    text_preview = models.TextField(null=False, blank=False)

    text = RedactorField(
        _('text'),
        allow_file_upload=True,
        allow_image_upload=True,
        blank=True,
        null=True
    )

    slug = models.SlugField(blank=True, null=True, max_length=500)

    publication_date = models.DateField(_('publication_date'), null=True,default=timezone.now)

    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def get_admin_thumbnail(self):
        return get_thumbnail(self.image,'100x100', quality=99).url

    def get_image_sm(self):
        return get_thumbnail(self.image,'520x260', quality=99).url

    def get_image(self):
        return get_thumbnail(self.image,'950x500', quality=99).url

    def get_absolute_url(self):
      return app_reverse('news_detail', 'news.urls', kwargs={
           'slug': self.slug,
        })

    def get_title(self):
        if len(self.title) > 35:
            words = self.title.split()
            final_sentence = ""
            verb_count = 0
            for w in words:
                verb_count = verb_count + len(w)
                final_sentence = final_sentence + w + " "
                if verb_count > 35:
                    break
            return final_sentence.strip() + "..."
        else:
            return self.title

    def get_text_preview(self):
            if len(self.text_preview) > 110:
                words = self.text_preview.split()
                final_sentence = ""
                verb_count = 0
                for w in words:
                    verb_count = verb_count + len(w)
                    final_sentence = final_sentence + w + " "
                    if verb_count > 110:
                        break
                return final_sentence.strip() + "..."
            else:
                return self.text_preview

    def save(self):
        if not self.slug:
            self.slug = str(self.order) + "-" + slugify(unidecode(self.title))
        super(News, self).save()

    def __str__(self):
       return self.title

    class Meta:
      verbose_name = _('News')
      verbose_name_plural = _('News')
      ordering = ('order',)
