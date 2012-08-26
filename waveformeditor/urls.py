from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView

from resources import CircuitResource

urlpatterns = patterns('',
    url(r'^$', 'waveformeditor.views.circuits_list', name='circuit_list'),
    url(r'^(?P<circuit_id>\d+)$', 'waveformeditor.views.show', name='circuit-item'),
)
