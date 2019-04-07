from modeltranslation.translator import translator, TranslationOptions
from blog.models import Blog_Post

class Blog_PostTranslationOptions(TranslationOptions):
    fields = ('name', 'content',)

translator.register(Blog_Post, Blog_PostTranslationOptions)