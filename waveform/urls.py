from django.conf.urls import patterns, include, url
from djangorestframework.resources import ModelResource
from waveformeditor.models import Circuit

from django.contrib import admin
admin.autodiscover()

class Circuits(ModelResource):
    model = Circuit


urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^circuits/', include('waveformeditor.urls')),
    url(r'^api/1.0/', include('api.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}),
    url(r'accounts/profile/$', 'waveformeditor.views.root_view'),
    url(r'^$','waveformeditor.views.root_view'),
)
