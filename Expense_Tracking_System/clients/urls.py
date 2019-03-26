from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signin$', views.userlogin, name='signin'),
    url(r'^signup$', views.usersignup, name='signup'),
    url(r'^logout$', views.userlogout, name='logout'),
]
