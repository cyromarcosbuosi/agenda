from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^add', views.add, name='add'),
    url(r'^read', views.read, name='read'),
]