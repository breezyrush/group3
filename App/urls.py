"""App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
<<<<<<< HEAD

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
=======
<<<<<<< HEAD

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Genre/$', 'music.views.view_genre'),

=======
from django.conf.urls import url
from music import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^view_performer/$', 'music.views.view_performer'),
>>>>>>> 16d42800e552f2319e04750c0a413ebc8b1f8269
>>>>>>> bbfc054bae8a20ebb7011618290c65909833971c
]
