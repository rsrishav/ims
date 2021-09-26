from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from main.constants import *
from masters.models import *
from django.contrib import messages
from django.core import serializers
import json


def get_all_category() -> dict:
    data = Category.objects.all()
    data = json.loads(serializers.serialize("json", data))
    return data


# Create your views here.
@login_required(login_url=URL_LOGIN)
def index(request):
    if request.method == "POST":
        data = request.POST.dict()
        data_model = Category(
            title=data.get("title"),
            description=data.get("description")
        )
        data_model.save()
        return JsonResponse(data_model.id, safe=False)
    else:
        return render(request, TMP_MASTERS_INDEX, {})


@login_required(login_url=URL_LOGIN)
def get_category_id(request):
    if request.method == "GET":
        try:
            next_id = Category.objects.latest("id").id + 1
            return JsonResponse({"success": True, "next_id": next_id})
        except Exception as e:
            if Category.objects.count() == 0:
                return JsonResponse({"success": True, "next_id": 1})
            return JsonResponse({"success": False, "error": str(e)})


@login_required(login_url=URL_LOGIN)
def category(request):
    if request.method == "POST":
        try:
            data = request.POST.dict()
            obj, created = Category.objects.update_or_create(pk=int(data.get("id")),
                                                             defaults={'title': data.get("title"),
                                                                       'description': data.get("description")},
                                                             )
            return JsonResponse({"success": True, "record_created": created, "record_updated": not created})
        except Exception as e:
            return JsonResponse({"success": False, "exception": str(e)})
    else:
        response = Category.get_all_records()
        return JsonResponse({"success": True, "data": response})
        # return HttpResponse(response, content_type='application/json')


@login_required(login_url=URL_LOGIN)
def get_color_id(request):
    if request.method == "GET":
        try:
            next_id = Color.objects.latest("id").id + 1
            return JsonResponse({"success": True, "next_id": next_id})
        except Exception as e:
            if Color.objects.count() == 0:
                return JsonResponse({"success": True, "next_id": 1})
            return JsonResponse({"success": False, "error": str(e)})


@login_required(login_url=URL_LOGIN)
def color(request):
    if request.method == "POST":
        try:
            data = request.POST.dict()
            obj, created = Color.objects.update_or_create(pk=int(data.get("id")),
                                                          defaults={'title': data.get("title"),
                                                                    'description': data.get("description")},
                                                          )
            return JsonResponse({"success": True, "record_created": created, "record_updated": not created})
        except Exception as e:
            return JsonResponse({"success": False, "exception": str(e)})
    else:
        response = Color.get_all_records()
        return JsonResponse({"success": True, "data": response})


@login_required(login_url=URL_LOGIN)
def get_size_id(request):
    if request.method == "GET":
        try:
            next_id = Size.objects.latest("id").id + 1
            return JsonResponse({"success": True, "next_id": next_id})
        except Exception as e:
            if Size.objects.count() == 0:
                return JsonResponse({"success": True, "next_id": 1})
            return JsonResponse({"success": False, "error": str(e)})


@login_required(login_url=URL_LOGIN)
def size(request):
    if request.method == "POST":
        try:
            data = request.POST.dict()
            obj, created = Size.objects.update_or_create(pk=int(data.get("id")),
                                                         defaults={'title': data.get("title"),
                                                                   'description': data.get("description")},
                                                         )
            return JsonResponse({"success": True, "record_created": created, "record_updated": not created})
        except Exception as e:
            return JsonResponse({"success": False, "exception": str(e)})
    else:
        response = Size.get_all_records()
        return JsonResponse({"success": True, "data": response})


@login_required(login_url=URL_LOGIN)
def get_package_id(request):
    if request.method == "GET":
        try:
            next_id = Package.objects.latest("id").id + 1
            return JsonResponse({"success": True, "next_id": next_id})
        except Exception as e:
            if Package.objects.count() == 0:
                return JsonResponse({"success": True, "next_id": 1})
            return JsonResponse({"success": False, "error": str(e)})


@login_required(login_url=URL_LOGIN)
def package(request):
    if request.method == "POST":
        try:
            data = request.POST.dict()
            obj, created = Package.objects.update_or_create(pk=int(data.get("id")),
                                                            defaults={'title': data.get("title")},
                                                            )
            return JsonResponse({"success": True, "record_created": created, "record_updated": not created})
        except Exception as e:
            return JsonResponse({"success": False, "exception": str(e)})
    else:
        response = Package.get_all_records()
        return JsonResponse({"success": True, "data": response})


@login_required(login_url=URL_LOGIN)
def get_style_id(request):
    if request.method == "GET":
        try:
            category_list = Category.get_all_records()
            next_id = Style.objects.latest("id").id + 1
            return JsonResponse({"success": True, "next_id": next_id, "category": category_list})
        except Exception as e:
            if Style.objects.count() == 0:
                return JsonResponse({"success": True, "next_id": 1, "category": category_list})
            return JsonResponse({"success": False, "error": str(e)})


@login_required(login_url=URL_LOGIN)
def style(request):
    if request.method == "POST":
        try:
            data = request.POST.dict()
            category_value = Category.objects.get(pk=int(data.get("fk_category")))
            obj, created = Style.objects.update_or_create(pk=int(data.get("id")),
                                                          defaults={'title': data.get("title"),
                                                                    'description': data.get("description"),
                                                                    'category': category_value},
                                                          )
            return JsonResponse({"success": True, "record_created": created, "record_updated": not created})
        except Exception as e:
            return JsonResponse({"success": False, "exception": str(e)})
    else:
        response = Style.get_all_records()
        for res in response:
            res["fields"]["category"] = Category.get_one(res["fields"]["category"])
        return JsonResponse({"success": True, "data": response})


@login_required(login_url=URL_LOGIN)
def get_hsn_code_id(request):
    if request.method == "GET":
        try:
            next_id = HSNCode.objects.latest("id").id + 1
            return JsonResponse({"success": True, "next_id": next_id})
        except Exception as e:
            if HSNCode.objects.count() == 0:
                return JsonResponse({"success": True, "next_id": 1})
            return JsonResponse({"success": False, "error": str(e)})


@login_required(login_url=URL_LOGIN)
def hsn_code(request):
    if request.method == "POST":
        try:
            data = request.POST.dict()
            obj, created = HSNCode.objects.update_or_create(pk=int(data.get("id")),
                                                            defaults={'title': data.get("title")},
                                                            )
            return JsonResponse({"success": True, "record_created": created, "record_updated": not created})
        except Exception as e:
            return JsonResponse({"success": False, "exception": str(e)})
    else:
        response = Package.get_all_records()
        return JsonResponse({"success": True, "data": response})
