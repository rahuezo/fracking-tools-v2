from django.conf.urls import url
from . import views


app_name = 'network_tools'


urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^build-events-networks', views.build_events_networks_view, name='build_enets'),
    url(r'^build-pairs-networks', views.build_pairs_networks_view, name='build_pnets'),
    url(r'^compare-networks', views.compare_networks_view, name='compare_nets'),
]
