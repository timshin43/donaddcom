from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	#url(r'^$', views.ad_donation, name="add_donation"),
	url(r'^$', views.donate_main, name="add_donation"),
	# url(r'^donate/$', views.donate, name="donate"),
	url(r'^project/(?P<donat_project_pk>\d+)/donate/$', views.donate, name="donate"),
	url(r'^project/(?P<donat_project_pk>\d+)/$', views.donate_project, name='donate_project'),
	url(r'^donate_test/$', views.donate, name="donate_test"),


	
]
