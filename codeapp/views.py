from django.shortcuts import render
from itemapp.models import Items
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from loginapp.decorator import unauthenticated_user, allowed_user, admin_only

# Create your views here.
@login_required(login_url='login')
@admin_only
def code_views(request):
    return render(request,'codeapp/code.html')

@login_required(login_url='login')
@admin_only
def qrbar_views(request, id):
    item = Items.objects.filter(id=id)
    return render(request,'itemapp/barcode.html',{'item':item})
