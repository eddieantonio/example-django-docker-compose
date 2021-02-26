from django.urls import path

from .views import index

appname = "api"

urlpatterns = [
    path("", index),
]
