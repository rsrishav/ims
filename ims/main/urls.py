from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.index, name="list"),
    path("", views.home, name="home"),
    path("create/", views.createRecord, name="create")
]
