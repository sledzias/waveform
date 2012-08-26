from django.conf.urls import patterns, include, url
from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from waveformeditor.models import Circuit


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

class Circuits(ModelResource):
    model = Circuit


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'waveform.views.home', name='home'),
    # url(r'^waveform/', include('waveform.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^circuits/', include('waveformeditor.urls')),
    url(r'^api/1.0/', include('api.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}),
    url(r'accounts/profile/$', 'waveformeditor.views.root_view'),
    url(r'^$','waveformeditor.views.root_view'),
)
