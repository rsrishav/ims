from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewItem
from django.contrib.auth.decorators import login_required
from main.constants import *


@login_required(login_url=URL_LOGIN)
def index(response):
    # ls = ToDoList.objects.get(id=id)
    ls = ToDoList.objects.all()
    return render(response, TMP_MAIN_LIST, {"ls": ls})


@login_required(login_url=URL_LOGIN)
def home(response):
    return render(response, TMP_MAIN_HOME, {})


@login_required(login_url=URL_LOGIN)
def createRecord(response):
    if response.method == "POST":
        form = CreateNewItem(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            t = ToDoList(name=name)
            t.save()
            return redirect(URL_LIST)
    else:
        form = CreateNewItem()
        return render(response, TMP_MAIN_CREATE, {"form": form})
