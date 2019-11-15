from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.success_main, name="success_main"),
	url(r'^(?P<s_story_pk>\d+)/$', views.s_story, name='s_story'),
	url(r'^tags/(?P<tag_pk>\d+)/$', views.tags, name='tags'),
]
