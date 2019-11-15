from modeltranslation.translator import translator, TranslationOptions
from ad_donation.models import Project_for_donations

class Project_for_donations_TranslationOptions(TranslationOptions):
    fields = ('name', 'content','short_description')

translator.register(Project_for_donations, Project_for_donations_TranslationOptions)