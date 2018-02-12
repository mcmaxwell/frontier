from modeltranslation.translator import translator, TranslationOptions
from .models import Info, MenuLinks
from common.translation import CommonPostTranslationOptions



class InfoTranslationOptions(TranslationOptions):
	fields = ('adress_footer','index_top_title', 'index_top_subtitle', 'news_top_title')

class MenuLinksTranslationOptions(TranslationOptions):
	fields = ('news_block_title','services_block_title', 'concept_block_title', 'references_block_title', 'contacts_block_title' )

translator.register(Info, InfoTranslationOptions)
translator.register(MenuLinks, MenuLinksTranslationOptions)
