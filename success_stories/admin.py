from django.contrib import admin
from .models import Success_stories, Tags
from modeltranslation.admin import TranslationAdmin

# Register your models here.

class BlogAdmin(TranslationAdmin):
    pass

admin.site.register(Tags)


# class TagStoryInLine(admin.TabularInline):
    # model = Tags.success_story.through


# class SuccessStoriesAdmin(admin.ModelAdmin):
    # fields = ['name', 'short_description', 'story_image', 'content', 'created_date', 'views_count']
    # inlines = [TagStoryInLine]




# admin.site.register(Success_stories, SuccessStoriesAdmin)
admin.site.register(Success_stories, BlogAdmin)
