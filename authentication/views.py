# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'authentication/home.html', {})

def login_user(request):
    return render(request, 'authentication/login.html', {})
