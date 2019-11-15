from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.funny_main, name="funny_main"),
	url(r'^(?P<fun_story_pk>\d+)/$', views.fun_story, name='fun_story'),
	url(r'^tags/(?P<tag_pk>\d+)/$', views.fun_tags, name='fun_tags'),
]
