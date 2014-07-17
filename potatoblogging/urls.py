from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^static(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^$', 'blog.views.index'),
    url(r'^blog/', include('blog.urls')),
    url(r'^myadmin/', include('myadmin.urls')),
)
