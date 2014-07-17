#coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from myadmin.models import Myuser
from myadmin.forms import LoginForm

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def out(request):
    logout(request)
    return HttpResponseRedirect('/')

def checklogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.data['username'], password=form.data['password']) 
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return render(request, 'login.html', {'form': form})
            else:
                return render(request, 'login.html', {'form': form})  
        else:
            return render(request, 'login.html', {'form': form})    
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form}) 

"""
def checklogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid(): 
            try:
                user = authenticate(username=form.data['username'], password=form.data['password'])
                if user is not None:
                    if user.is_active:
                        auth_login(request, user)
                        return HttpResponseRedirect('/')
                    else:
                        return render(request, 'login.html', {'form': form})
                else:
                    return render(request, 'login.html', {'form': form})
            except: 
                return render(request, 'login.html', {'form': form})   
        else:
            return render(request, 'login.html', {'form': form})    
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form}) 
"""
