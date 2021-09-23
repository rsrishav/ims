from django.urls import path
from main.constants import *
from . import views

urlpatterns = [
    path("", views.index, name=NAMES_MASTERS_INDEX),
    path("category/", views.category, name=NAMES_MASTERS_CATEGORY),
    path("color/", views.color, name=NAMES_MASTERS_COLOR),
    # path("list/", views.index, name="list"),
    # path("create/", views.createRecord, name="create")
]
