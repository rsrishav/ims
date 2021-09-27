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
    path("package/", views.package, name=NAMES_MASTERS_PACKAGE),
    path("package/getid", views.get_package_id, name=NAMES_MASTERS_PACKAGE_ID),
    path("style/", views.style, name=NAMES_MASTERS_STYLE),
    path("style/getid", views.get_style_id, name=NAMES_MASTERS_STYLE_ID),
    path("hsn_code/", views.hsn_code, name=NAMES_MASTERS_HSN_CODE),
    path("hsn_code/getid", views.get_hsn_code_id, name=NAMES_MASTERS_HSN_CODE_ID),

]
