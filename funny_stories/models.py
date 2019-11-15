from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class FunnyStories(models.Model):
    name = models.CharField(max_length=500)
    content = RichTextUploadingField(blank=True)
    short_description = models.CharField(max_length=500)
    story_image = models.ImageField(upload_to="uploads/success_stories_icons/")
    views_count = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name


class FunStorTag(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500, blank=True)
    created_date = models.DateTimeField(default=timezone.now())
    funny_story = models.ManyToManyField(FunnyStories, related_name='tags', blank=True)

    def __str__(self):
        return self.name
