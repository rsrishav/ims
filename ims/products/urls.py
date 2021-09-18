from django.urls import path
from main.constants import *
from . import views

urlpatterns = [
    path("", views.index, name="products_add"),
    path("add/", views.add, name="products_add"),
    # path("list/", views.index, name="list"),
    # path("create/", views.createRecord, name="create")
]
