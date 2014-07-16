from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'login'),
    url(r'^checklogin/$', 'checklogin'),
    url(r'^logon/$', 'logon'),
    url(r'^logoff/$', 'logoff'),
)