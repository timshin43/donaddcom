from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name="hom_page"),
    url(r'^data_analysis/$', views.data_analysis, name="data_analysis"),
    url(r'^metrics/$', views.metrics, name="metrics"),
    url(r'^about_us/$', views.about_us, name="about_us"),
    url(r'^contacts/$', views.contacts, name="contacts"),
    url(r'^data/$', views.data, name="data"),
    url(r'^get_csv_data/$', views.get_csv_data, name="get_csv_data"),
    url(r'^page_not_found/$', views.page_not_found, name="page_not_found"),
	url(r'^change_language/$', views.change_language, name="change_language"),



]
