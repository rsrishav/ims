from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from main.constants import *
from masters.models import *
from django.contrib import messages


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
def category(request):
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
