from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^newpost/$', 'newpost'),
    url(r'^newpost/save/$', 'newpost_save'),
)