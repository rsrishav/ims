from django.shortcuts import render
from main.constants import *
from django.contrib.auth.decorators import login_required


@login_required(login_url=URL_LOGIN)
def index(response):
    return render(response, TMP_PROD_INDEX, {})


@login_required(login_url=URL_LOGIN)
def add(response):
    return render(response, TMP_PROD_ADD, {})
