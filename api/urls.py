from django.conf.urls.defaults import patterns, url
from views import CircuitInstanceView, CircuitListView
urlpatterns = patterns('',
    url(r'^circuits$', CircuitListView.as_view(), name='circuits_api_root'),
    url(r'^circuits/(?P<id>[0-9]+)$', CircuitInstanceView.as_view(), name='circuits_api_instance'),
)
