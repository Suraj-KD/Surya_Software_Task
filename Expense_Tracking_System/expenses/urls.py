from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.dashboard, name='create'),
    url(r'^read$', views.read, name='read'),
    url(r'^view$', views.viewall, name='view'),
    url(r'^viewrow$', views.viewrow, name='viewrow')
]