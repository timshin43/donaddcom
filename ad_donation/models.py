from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from accounts.models import AppUser
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Total_donation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    amount = models.FloatField(blank=True)

    def __str__(self):
        return self.name

class Project_for_donations(models.Model):
	name = models.CharField(max_length=500)
	content = RichTextUploadingField(blank=True)
	short_description = models.CharField(max_length=500)
	project_image = models.ImageField(upload_to="uploads/project_for_donations/")
	views_count = models.PositiveIntegerField(default=0)
	amount_required = models.FloatField(default=0, blank=True)
	amount_donated = models.FloatField(default=0,blank=True)
	percentage_donated = models.FloatField(default=0,blank=True)
	created_date = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.name


class Donations(models.Model):
	amount = models.FloatField(blank=True)
	who_donated = models.ForeignKey(User, on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=timezone.now())
	project = models.ManyToManyField(Project_for_donations, related_name='project_donation', blank=True)

	def __str__(self):
		return self.who_donated.username

		
		
class Video(models.Model):
	name = models.CharField(max_length=300, blank=True)
	description = models.CharField(max_length=1000, blank=True)
	company_name = models.CharField(max_length=500, blank=True)
	link = models.CharField(max_length=1000, blank=True)
	language = models.CharField(max_length=50, default='ru')
	views_count = models.PositiveIntegerField(default=0)
	video = EmbedVideoField()
	project = models.ManyToManyField(Project_for_donations, related_name='project_video', blank=True)
	#owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	owner = models.OneToOneField(User, related_name='app_user', default=1, on_delete=models.CASCADE)
	is_active = models.BooleanField(blank=True, default=False)
	is_deleted = models.BooleanField(blank=True, default=False)

	def __str__(self):
		return self.name




