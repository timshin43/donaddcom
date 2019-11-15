from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Single_Page(models.Model):
    title = models.CharField(max_length=500)
    content = RichTextUploadingField(blank=True)
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title
