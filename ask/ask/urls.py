from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','qa.voews.test'),
	url(r'^login/$','qa.voews.test'),	
	url(r'^signup$','qa.voews.test'),
	url(r'^question/(\d+)$','qa.voews.test'),	
	url(r'^ask$/.','qa.voews.test'),	
	url(r'^popular/$','qa.voews.test'),	
	url(r'^new/$','qa.voews.test'),
)
