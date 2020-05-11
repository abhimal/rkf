from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from account.models import Account
from itemapp.models import Sales
from userapp.forms import UserForm
from django.contrib.auth.decorators import login_required
from loginapp.decorator import unauthenticated_user, allowed_user, admin_only
from django.contrib.auth.models import Group
from django.db.models import Count, Sum, Avg
from django.http import JsonResponse

@login_required(login_url='login')
@admin_only
def users_views(request):
    context = {}
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            mobile_number = form.cleaned_data.get('mobile_number')
            raw_password = form.cleaned_data.get('password1')

            group = Group.objects.get(name='user')
            user.groups.add(group)

            # account = authenticate(mobile_number = mobile_number, password = raw_password)
            # login(request,account)

            messages.success(request,'New user created successfully!')
            return redirect('/users')
        else:
            # context['users_form'] = form
            messages.error(request,form.errors)
            return redirect('/users')
    else:
        form = UserForm()
        context['users_form'] = form
        return render(request,'userapp/users.html',context)

@login_required(login_url='login')
@admin_only
def search_user_views(request):
    users = Account.objects.all().order_by('id')
    return render(request,'userapp/searchuser.html', {'users':users})

@login_required(login_url='login')
#@admin_only
def sales_user_record_views(request):
    if request.method == 'POST':
        users = Account.objects.all()
        username = request.POST['user_name']

        total_comission = Sales.objects.filter(salesman=username).aggregate(Sum('comission'))
        total_sale = Sales.objects.filter(salesman=username).aggregate(Sum('sale_price'))

        comission = total_comission['comission__sum']
        sale = total_sale['sale_price__sum']

        return render(request,'userapp/userrecord.html',{'users':users, 'comission':comission, 'sale':sale, 'username':username})
    else:
        users = Account.objects.all()
        return render(request,'userapp/userrecord.html',{'users':users})

@login_required(login_url='login')
def get_User_views(request):
    if request.method == "GET" and request.is_ajax():
        username = request.GET.get("username")
        try:
            total_comission = Sales.objects.filter(salesman=username).aggregate(Sum('comission'))
            total_sale = Sales.objects.filter(salesman=username).aggregate(Sum('sale_price'))

            comission = total_comission['comission__sum']
            sale = total_sale['sale_price__sum']
        except:
            return JsonResponse({"success":False}, status=400)
        user_info = {
        "user_name": username,
        "total_sale": sale,
        "total_comission": comission
        }
        return JsonResponse({"user_info":user_info}, status=200)
    return JsonResponse({"success":False}, status=400)
