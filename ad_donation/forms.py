from django import forms
from ad_donation.models import Total_donation, Video, Donations, Project_for_donations
from .models import AppUser
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from django.forms import extras

class NewAdvertisementForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('name', 'description', 'video', 'company_name', 'link', 'language')
