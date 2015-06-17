"""mysite URL Configuration

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
from blog import urls as blog_urls

urlpatterns = [
    url(r'^$', 'mysite.views.home', name='home'),
    url(r'^project$', 'mysite.views.project', name='project'),
    url(r'^about$', 'mysite.views.about', name='about'),
    url(r'^about/bear$', 'mysite.views.about', name='about'),
    url(r'^resume$', 'mysite.views.resume', name='resume'),
    url(r'^upload$', 'mysite.views.upload', name='upload'),
    url(r'^test$', 'mysite.views.test', name='test'),
    url(r'^blog/', include(blog_urls))
]

handler404 = 'mysite.views.error404'
