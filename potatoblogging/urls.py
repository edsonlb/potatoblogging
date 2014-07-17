from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^media(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    #url(r'^static(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^$', 'blog.views.index'),
    url(r'^blog/', include('blog.urls')),
    url(r'^myadmin/', include('myadmin.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
