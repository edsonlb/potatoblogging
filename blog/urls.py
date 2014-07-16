from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^post/$', 'post'),
    url(r'^post/save/$', 'post_save'),
    url(r'^post/(?P<postName>[^/]+)/$', 'post_view'),
    url(r'^post/delete/(?P<id>\d+)/$', 'post_delete'),
    url(r'^post/edit/(?P<id>\d+)/$', 'post_edit'),
    url(r'^search/$', 'post_search'),
    url(r'^offline/$', 'post_offline'),
)