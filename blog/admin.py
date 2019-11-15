from django.contrib import admin
from .models import Blog_Post
from modeltranslation.admin import TranslationAdmin
# Register your models here.

# admin.site.register(Blog_Post)

class BlogAdmin(TranslationAdmin):
    pass

admin.site.register(Blog_Post, BlogAdmin)