from django.urls import include, path
from django.shortcuts import render
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path('flights/', views.flights, name="flights"),
    path("back/", views.back, name="back"),
    path("wiki/", views.wiki, name="wiki"),
    path("wiki/<str:wiki>", views.default, name="default"),
    path("search/", views.search, name="search"),
    path("new/", views.new, name="new"),
    path("random/", views.randy, name="random"),
    path("wiki/<str:entry>/edit", views.edit, name="edit"),
]
urlpatterns += staticfiles_urlpatterns()