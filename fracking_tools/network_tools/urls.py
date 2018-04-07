from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'network_tools'


urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^results/$', views.results_view, name='results'),
    url(r'^build-events/$', views.build_events_view, name='build_events'),
    url(r'^build-events/build/', views.build_events_now_view, name='build_events_now'),
    url(r'^build-events-networks/', views.build_events_networks_view, name='build_enets'),
    url(r'^build-pairs-networks/$', views.build_pairs_networks_view, name='build_pnets'),
    url(r'^compare-networks/$', views.compare_networks_view, name='compare_nets'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
