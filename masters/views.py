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
def getCategoryID(request):
    if request.method == "GET":
        try:
            next_id = Category.objects.latest("id").id + 1
            return JsonResponse({"success": True, "next_id": next_id})
        except Exception as e:
            return JsonResponse({"success": True, "error": str(e)})


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
        return JsonResponse({"success": False, "data": response})


@login_required(login_url=URL_LOGIN)
def getColorID(request):
    if request.method == "GET":
        try:
            next_id = Color.objects.latest("id").id + 1
            return JsonResponse({"success": True, "next_id": next_id})
        except Exception as e:
            return JsonResponse({"success": True, "error": str(e)})


@login_required(login_url=URL_LOGIN)
def color(request):
    if request.method == "POST":
        try:
            data = request.POST.dict()
            data_model = Category(
                title=data.get("title"),
                description=data.get("description")
            )
            data_model.save()
            return JsonResponse({"success": True}, safe=False)
        except:
            return JsonResponse({"success": False}, safe=False)
    else:
        return render(request, TMP_MASTERS_INDEX, {})
