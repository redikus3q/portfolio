from django.urls import include, path
from django.shortcuts import render
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:wiki>", views.default, name="default"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("random", views.randy, name="random"),
    path("wiki/<str:entry>/edit", views.edit, name="edit"),
]