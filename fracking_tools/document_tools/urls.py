from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'document_tools'


urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^ajax/check-task-status/', views.check_task_status, name='check_task_status'),    
    # url(r'^results/$', views.results_view, name='results'),
    
    url(r'^compare-documents/$', views.compare_documents_view, name='compare_documents'),
    url(r'^compare-documents/compare/$', views.compare_documents_now_view, name='compare_documents_now'),
    url(r'^compare-documents/download/$', views.download_document_comparisons_view, name='download_comparisons'),

    url(r'^tag-documents-keywords/$', views.tag_documents_keywords_view, name='tag_documents_keywords'),
    url(r'^tag-documents-keywords/tag$', views.tag_documents_keywords_now_view, name='tag_documents_keywords_now'),
    
    url(r'^tag-documents-ner/$', views.tag_documents_ner_view, name='tag_documents_ner'),
    url(r'^tag-documents-ner/tag$', views.tag_documents_ner_now_view, name='tag_documents_ner_now'),

    url(r'^compute-document-statistics/$', views.compute_document_statistics_view, name='compute_document_statistics'),
    url(r'^compute-document-statistics/compute$', views.compute_document_statistics_now_view, name='compute_document_statistics_now'),

    url(r'^compute-document-statistics/download$', views.download_document_analysis_view, name='download_document_analysis'),


    url(r'^download-tagged-documents$', views.download_tagged_documents_view, name='download_tagged_documents'),



    # download_keywords_tagged_documents_view
    # url(r'^compare-documents/compare/$', views.compare_documents_now_view, name='compare_documents_now'),
    # url(r'^compare-documents/download/$', views.download_document_comparisons_view, name='download_comparisons'),
    

    # tag_documents_keywords_view
    # url(r'^events-networks/$', views.build_events_networks_view, name='build_enets'),
    # url(r'^events-networks/build/$', views.build_events_networks_now_view, name='build_enets_now'),
    
    # url(r'^pairs-networks/$', views.build_pairs_networks_view, name='build_pnets'),
    # url(r'^pairs-networks/build/$', views.build_pairs_networks_now_view, name='build_pnets_now'),
    
    # url(r'^compare-networks/$', views.compare_networks_view, name='compare_nets'),
    # url(r'^compare-networks/compare$', views.compare_networks_now_view, name='compare_nets_now'),
    # url(r'^compare-networks/download$', views.download_network_comparisons_view, name='download_comparisons'),

    # url(r'^download/$', views.download_networks_view, name='download_networks'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
