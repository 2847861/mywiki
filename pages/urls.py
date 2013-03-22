from django.conf.urls import patterns, url
from pages.models import Page
from pages import views

urlpatterns = patterns('',
    url(r'^$', views.Home, name=''),
    url(r'^History/$', views.article1, name='History'),
    url(r'^Health/$', views.article2, name='Health'),
)