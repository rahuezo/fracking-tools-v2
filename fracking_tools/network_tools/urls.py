from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'network_tools'


urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^ajax/check-task-status/', views.check_task_status, name='check_task_status'),    
    url(r'^results/$', views.results_view, name='results'),
    
    url(r'^events/$', views.build_events_view, name='build_events'),
    url(r'^events/build/$', views.build_events_now_view, name='build_events_now'),
    url(r'^events/download/$', views.download_events_file_view, name='download_events'),
    
    url(r'^events-networks/$', views.build_events_networks_view, name='build_enets'),
    url(r'^events-networks/build/$', views.build_events_networks_now_view, name='build_enets_now'),
    
    url(r'^pairs-networks/$', views.build_pairs_networks_view, name='build_pnets'),
    url(r'^pairs-networks/build/$', views.build_pairs_networks_now_view, name='build_pnets_now'),
    
    url(r'^compare-networks/$', views.compare_networks_view, name='compare_nets'),
    url(r'^compare-networks/compare$', views.compare_networks_now_view, name='compare_nets_now'),
    url(r'^compare-networks/download$', views.download_network_comparisons_view, name='download_comparisons'),

    url(r'^download/$', views.download_networks_view, name='download_networks'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
