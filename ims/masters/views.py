from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from main.constants import *


# Create your views here.
@login_required(login_url=URL_LOGIN)
def index(response):
    return render(response, TMP_MASTERS_INDEX, {})
