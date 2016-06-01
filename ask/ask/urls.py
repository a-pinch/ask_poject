from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'qa.views.main', name='main'),
    url(r'^login/$', 'qa.views.login'),
    url(r'^signup/$', 'qa.views.signup'),
    url(r'^question/(\d+)/$', 'qa.views.question', name='quest'),
    url(r'^ask/.*$', 'qa.views.ask'),
    url(r'^popular/$', 'qa.views.popular', name='popular'),
    url(r'^/answer/$', 'qa.views.answer'),

)
