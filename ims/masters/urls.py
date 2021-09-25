from django.urls import path
from main.constants import *
from . import views

urlpatterns = [
    path("", views.index, name=NAMES_MASTERS_INDEX),
    path("category/", views.category, name=NAMES_MASTERS_CATEGORY),
    path("category/getid", views.get_category_id, name=NAMES_MASTERS_CATEGORY_ID),
    path("color/", views.color, name=NAMES_MASTERS_COLOR),
    path("color/getid", views.get_color_id, name=NAMES_MASTERS_COLOR_ID),
    path("size/", views.size, name=NAMES_MASTERS_SIZE),
    path("size/getid", views.get_size_id, name=NAMES_MASTERS_SIZE_ID),
    # path("list/", views.index, name="list"),
    # path("create/", views.createRecord, name="create")
]
