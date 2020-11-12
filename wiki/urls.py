
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("encyclopedia.urls")),
    path("google/", include("google.urls")),
]
