from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'euro.views.home', name='home'),
    url(r'^web/', include('web.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
