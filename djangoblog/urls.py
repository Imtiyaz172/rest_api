"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blogapp import views
from django.contrib.sitemaps.views import sitemap
from blogapp.sitemap import *

sitemaps = {
    "indexSitemap" : indexSitemap,
    "aboutSitemap" : aboutSitemap,
    "contactSitemap" : contactSitemap,
    "loginSitemap" : loginSitemap,
    "registerSitemap" : registerSitemap,
    "dashboardSitemap" : dashboardSitemap,
    "historySitemap" : historySitemap,
    "classSitemap" : classSitemap,
    "subjectSitemap" : subjectSitemap,
    "questionSitemap" : questionSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("blogapp.api.urls")),
    path('',include("blogapp.urls")),
    path('sitemap.xml/', sitemap, {'sitemaps':sitemaps}),
    path('ckeditor',include("ckeditor_uploader.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)