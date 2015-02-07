'''
Used to redirect the calls whenever a request hits a particular URL
'''
from django.conf.urls import patterns, include, url
from django.contrib import admin
from pathshala.question_view import test

urlpatterns = patterns('',
    # Examples:
    url(r'^test/', test),
    url(r'^admin/', include(admin.site.urls)),
)
