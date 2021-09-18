from django.shortcuts import render
from main.constants import *
from django.contrib.auth.decorators import login_required


@login_required(login_url=URL_LOGIN)
def index(response):
    return render(response, TMP_PROD_INDEX, {})


@login_required(login_url=URL_LOGIN)
def add(response):
    if response.method == "POST":
        # form = CreateNewItem(response.POST)
        # if form.is_valid():
        #     name = form.cleaned_data["name"]
        #     t = ToDoList(name=name)
        #     t.save()
        #     return redirect(URL_LIST)
        return render(response, TMP_PROD_ADD, {})
    else:
        return render(response, TMP_PROD_ADD, {})
