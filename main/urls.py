from django.conf.urls import url
from .import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.index),
    url(r'^create', views.create),
    url(r'^delete/(?P<id>\d+)$', views.destroy),
    path('update', views.update),

]