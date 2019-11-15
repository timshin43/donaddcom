from modeltranslation.translator import translator, TranslationOptions
from success_stories.models import Success_stories

class Success_stories_TranslationOptions(TranslationOptions):
    fields = ('name', 'content','short_description')

translator.register(Success_stories, Success_stories_TranslationOptions)