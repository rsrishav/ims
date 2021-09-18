from django.shortcuts import render, redirect
from .forms import RegisterForm
from main.constants import *


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect(URL_LOGIN)
    else:
        form = RegisterForm()
    return render(response, TMP_REGISTER, {"form": form})
