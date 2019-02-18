# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'authentication/home.html', {})

def login_user(request):
    print 'in login_user'
    print request.method
    if request.method == 'POST':
        print 'in POST'
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print 'user not none'
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            print 'oops user None'
            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})
