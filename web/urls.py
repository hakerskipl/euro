from django.conf.urls import patterns, url, include
from web.views import *

urlpatterns = patterns('',
	url('^home/$', home, name='home')
)