from django.shortcuts import render
from main.constants import *
from django.contrib.auth.decorators import login_required
from masters import models as master_model


@login_required(login_url=URL_LOGIN)
def index(response):
    return render(response, TMP_PROD_INDEX, {})


@login_required(login_url=URL_LOGIN)
def add(response):
    if response.method == "POST":
        return render(response, TMP_PROD_ADD, {})
    else:
        category = master_model.Category.get_all_records()
        return render(response, TMP_PROD_ADD, {"category": category})
