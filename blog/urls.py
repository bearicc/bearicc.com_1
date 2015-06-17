from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^category/(?P<category>[\w|\W]+)$', 'blog.views.category', name='category'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/(?P<title>[\w|\W]+)$', 'blog.views.article', name='article'),
    url(r'^admin/', include(admin.site.urls))
]

admin.site.site_header = 'Login in'
