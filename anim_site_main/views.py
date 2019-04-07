from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from anim_site_main.models import Single_Page
from ad_donation.models import Donations
from accounts.models import AppUser
from django.contrib.auth.models import User
import csv
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *
from django.utils import  translation


# Create your views here.

def home(request):
	# user_language = "ru"
	# translation.activate(user_language)
	# request.session[translation.LANGUAGE_SESSION_KEY] = user_language
	return render(request, "anim_site_main/homepage.html")


def about_us(request):
	try:
		about_us = get_object_or_404(Single_Page, title='About Us')
	except:
		about_us = get_object_or_404(Single_Page, title='О нас')
	return render(request, "anim_site_main/about_us.html", {"about_us": about_us})

def contacts(request):
	try:
		contacts = get_object_or_404(Single_Page, title='Contacts')
	except:
		contacts = get_object_or_404(Single_Page, title='Контакты')
	return render(request, "anim_site_main/contacts.html", {"contacts": contacts})

def metrics(request):
    # The scope for the OAuth2 request.
    SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'

    # The location of the key file with the key data.
    # KEY_FILEPATH = 'chromatic-force-214123-9171969eb23d.json'
    KEY_FILEPATH = 'donaddcomga-c70de7e09f93.json'

    # Defines a method to get an access token from the ServiceAccount object.
    token = ServiceAccountCredentials.from_json_keyfile_name(
            KEY_FILEPATH, SCOPE).get_access_token().access_token
    # string ="file:::"+ KEY_FILEPATH +",,,token::::"+token
    # return HttpResponse(string)
    return render(request, "anim_site_main/metrics.html", {"token":token})


def data(request):
    return render(request, "anim_site_main/data.html")


def data_analysis(request):
    return render(request, "anim_site_main/data_analysis.html")


def get_csv_data(request):
    all_donations = Donations.objects.all()
    columns = ["donation id", "donation amount", "donatior user id", "donation date"]
    donations_list = []
    for donation in all_donations:
        donations_list.append([donation.id,donation.amount,donation.who_donated.id,donation.created_date])
    donation_file = open('all_donations.csv', 'w', newline='')
    with donation_file:
        writer = csv.writer(donation_file)
        writer.writerows([columns])
        writer.writerows(donations_list)
    all_users = User.objects.all()
    columns_users = ["user_id", "User Country", "User State", "User birth_date"]
    user_list=[]
    for user in all_users:
        user_list.append([user.id, user.app_user.country, user.app_user.state, user.app_user.birth_date])
    user_file = open('all_users.csv', 'w', newline='')
    with user_file:
        writer = csv.writer(user_file)
        writer.writerows([columns_users])
        writer.writerows(user_list)
    return render(request, "anim_site_main/get_csv_data.html", {"all_users": all_users})

def error_404(request):
    data = {}
    return render(request, 'anim_site_main/404_error.html', data)

def page_not_found(request):

    return render(request, "anim_site_main/404_error.html")
	
def change_language(request):
	return redirect(about_us)