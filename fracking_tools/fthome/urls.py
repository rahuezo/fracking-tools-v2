from django.conf.urls import url
from . import views


app_name = 'fthome'


urlpatterns = [
    url(r'^$', views.index_view, name='index'),
]
