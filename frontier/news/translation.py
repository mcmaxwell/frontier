from modeltranslation.translator import translator, TranslationOptions
from .models import News
from common.translation import CommonPostTranslationOptions


class NewsTranslationOptions(TranslationOptions):
	fields = ('title', 'text_preview', 'text')

translator.register(News, NewsTranslationOptions)