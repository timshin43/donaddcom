from modeltranslation.translator import translator, TranslationOptions
from anim_site_main.models import Single_Page

class Single_Page_TranslationOptions(TranslationOptions):
    fields = ('title', 'content')

translator.register(Single_Page, Single_Page_TranslationOptions)