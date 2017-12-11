from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^add', views.add, name='add'),
    url(r'^read', views.read, name='read'),
    url(r'^search', views.read, name='read'),
    url(r'^alter', views.alter, name='alter'),
    url(r'^delete', views.delete, name='delete'),
    url(r'test', views.test, name='test')
]
