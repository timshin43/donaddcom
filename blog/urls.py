from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.blog_main, name="blog_main"),
	url(r'^(?P<blog_post_pk>\d+)/$', views.blog_post, name='blog_post'),

]
