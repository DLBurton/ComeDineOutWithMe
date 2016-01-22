__author__ = 'darrenburton'

from django.conf.urls import patterns, url

urlpatterns = patterns('project.homepage.views',
    url(r'^$', 'common', name='home'),
)