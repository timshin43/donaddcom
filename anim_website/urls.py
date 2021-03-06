"""anim_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:s
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from anim_site_main import views as anim_site_main_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
                  # url(r'^$', anim_site_main_views.home, name="home"),
                  url(r'^admin/', admin.site.urls),
                  url(r'', include('anim_site_main.urls')),
                  url(r'success_stories/', include('success_stories.urls')),
                  url(r'add_donation/', include('ad_donation.urls')),
                  url(r'accounts/', include('accounts.urls')),
                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),
                  url(r'^why_we_like_animals/', include('funny_stories.urls')),
                  url(r'^blog/', include('blog.urls')),
				  url(r'^i18n/', include('django.conf.urls.i18n')),

              ]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = anim_site_main_views.error_404
