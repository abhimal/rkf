from django.shortcuts import render
from itemapp.models import Items
from itemapp.models import Sales
from django.contrib.auth.decorators import login_required
from loginapp.decorator import unauthenticated_user, allowed_user, admin_only
from django.db.models import Count, Sum, Avg, Max
from datetime import timedelta, datetime
from django.db.models import F


@login_required(login_url='login')
# @allowed_user(allowed_roles=['admin'])
@admin_only
def dash_views(request):
    data = []
    total_sale = Sales.objects.all().order_by('-id').aggregate(Sum('sale_price'))
    sale = total_sale['sale_price__sum']

    totalamount = Items.objects.all().order_by('-id').aggregate(Sum('total_amount'))
    amount = totalamount['total_amount__sum']
    records = Sales.objects.all().order_by('-id')[:5]

    top_sale_I = Items.objects.all().aggregate(Max('item_level'))
    topI = top_sale_I['item_level__max']
    topitem = Items.objects.filter(item_level=topI)
    topitem = topitem[0:1]

    items = Items.objects.all()
    for item in items:
        if item.item_quantity == 5 or int(item.item_quantity)<5:
            data.append(item)
    today = datetime.now()
    today.strftime("%B / %d / %Y : %H:%M")

    return render(request,'dashboardapp/dash.html',{'sale':sale, 'records':records, 'data':data, 'amount':amount, 'topitem':topitem, 'today':today})
