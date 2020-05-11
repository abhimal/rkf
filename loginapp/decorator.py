from django.http import HttpResponse
from django.shortcuts import render, redirect
from account.models import Account

def unauthenticated_user(view_fun):
    def wrapper_fun(request, *args, **kwargs):

        if request.user.is_authenticated:
            if request.user.is_admin:
                return redirect('/dashboard')
            else:
                return redirect('/salesman')
        else:
            return view_fun(request, *args, **kwargs)

    return wrapper_fun

def allowed_user(allowed_roles=[]):
    def decorator(view_fun):
        def wrapper_fun(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_fun(request, *args, **kwargs)
            else:
                return HttpResponse('you are not authorized to use this page')
        return wrapper_fun
    return decorator

def admin_only(view_fun):
    def wrapper_fun(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'admin':
            return view_fun(request, *args, **kwargs)
        if group == 'user':
            return redirect('/salesman')
    return wrapper_fun
