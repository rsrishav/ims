from django.urls import path
from main.constants import *
from . import views

urlpatterns = [
    path("", views.index, name=NAMES_MASTERS_INDEX),
    path("category/", views.category, name=NAMES_MASTERS_CATEGORY),
    path("category/getid", views.getCategoryID, name=NAMES_MASTERS_CATEGORY_ID),
    path("color/", views.color, name=NAMES_MASTERS_COLOR),
    path("color/getid", views.getColorID, name=NAMES_MASTERS_COLOR_ID),
    # path("list/", views.index, name="list"),
    # path("create/", views.createRecord, name="create")
]
    