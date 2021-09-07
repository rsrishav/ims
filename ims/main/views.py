from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewItem
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(response):
    # ls = ToDoList.objects.get(id=id)
    ls = ToDoList.objects.all()
    return render(response, "main/list.html", {"ls": ls})


@login_required(login_url='/login/')
def home(response):
    return render(response, "main/home.html", {})


def createRecord(response):
    if response.method == "POST":
        form = CreateNewItem(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            t = ToDoList(name=name)
            t.save()
            return redirect("/list")
    else:
        form = CreateNewItem()
        return render(response, "main/create.html", {"form": form})
