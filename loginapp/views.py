from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from account.models import Account
from django.contrib import messages
from .decorator import unauthenticated_user

# Create your views here.
def login_views(request):
    if request.method == 'POST':
        mobilenumber = request.POST['mobnumber']
        user_psw = request.POST['psw']
        user = authenticate(mobile_number=mobilenumber, password=user_psw)
        if user is not None:
            if user.is_admin:
                login(request, user)
                return redirect('/dashboard')
            else:
                login(request, user)
                return redirect('/salesman')

        else:
            messages.warning (request,'invalid mobile number and password')
            return redirect('/')
    else:
        return render(request,'loginapp/login.html')
@unauthenticated_user
def login_page_views(request):
    return render(request,'loginapp/login.html')

def logout_views(request):
    logout(request)
    return redirect('/')
