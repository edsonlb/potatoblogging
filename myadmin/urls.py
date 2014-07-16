from django.conf.urls import patterns, include, url

urlpatterns = patterns('myadmin.views',
    url(r'^$', 'login'),
    url(r'^checklogin/$', 'checklogin'),
    url(r'^logoff/$', 'logoff'),
)