from django.conf.urls import url
from . import views


app_name = 'documentation'


urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^edit/$', views.edit_view, name='edit'),
    url(r'^add-category/$', views.add_category_view, name='add_category'),
    url(r'^add-section/$', views.add_section_view, name='add_section'),
]
