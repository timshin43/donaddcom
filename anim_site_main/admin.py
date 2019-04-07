from django.contrib import admin
from .models import Single_Page
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class BlogAdmin(TranslationAdmin):
    pass

admin.site.register(Single_Page,BlogAdmin)