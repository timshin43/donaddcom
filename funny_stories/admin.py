from django.contrib import admin
from .models import FunnyStories, FunStorTag

# Register your models here.

admin.site.register(FunStorTag)


class FunTagStoryInLine(admin.TabularInline):
    model = FunStorTag.funny_story.through


class FunnyStoriesAdmin(admin.ModelAdmin):
    fields = ['name', 'short_description', 'story_image', 'content', 'created_date', 'views_count']
    inlines = [FunTagStoryInLine]


admin.site.register(FunnyStories, FunnyStoriesAdmin)
