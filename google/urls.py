from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.default, name="default"),
    path("advanced", views.advanced, name="advanced"),
    path("images", views.images, name="images"),
]