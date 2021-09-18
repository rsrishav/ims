from django.urls import path
from main.constants import *
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.index, name="list"),
    path("create/", views.createRecord, name="create")
]
