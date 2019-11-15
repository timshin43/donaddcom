from django.contrib import admin
from .models import Total_donation, Video, Donations, Project_for_donations
from embed_video.admin import AdminVideoMixin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline, TranslationGenericStackedInline



# Register your models here.
# this video class is required to show video field in an admin panel
class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
	
class BlogAdmin(TranslationAdmin):
    pass
	
admin.site.register(Total_donation)
admin.site.register(Donations)
admin.site.register(Video, VideoAdmin)
admin.site.register(Project_for_donations,BlogAdmin)
