from django.shortcuts import render
from itemapp.models import Items, Sales, Return
from account.models import Account
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from loginapp.decorator import unauthenticated_user, allowed_user, admin_only
from django.utils.datastructures import MultiValueDictKeyError
from .filters import SaleFilter, ReturnFilter
from .render import Render
from django.views import View
class PdfSale(View):
    def get(self, request):
        records = Sales.objects.all()
        params = {
            'records': records,
            'request': request
        }
        return Render.render('salesmanapp/pdf.html', params)

@login_required(login_url='login')
def salesman_views(request):
    if request.method == 'POST':
        if 'isale' in request.POST:
            saleprice = request.POST['sale_close']
            item_code = request.POST['icode']
            salesman_name = request.POST['sale_man']
            mobile_number = request.POST['mobnumber']
            try:
                exchange = request.POST['exchange_item']
            except MultiValueDictKeyError:
                exchange = False

            percent = int(saleprice) * 1/100

            item_id = Items.objects.get(item_code=item_code)
            shopname = item_id.shop_name


            sales_info = Sales(item_code=item_code, salesman=salesman_name, mobile_number=mobile_number,
            sale_price=saleprice, comission=percent, exchange_item=exchange,shop_name=shopname)

            item_id = Items.objects.get(item_code=item_code)
            id = item_id.id

            sales_info.sales_id_id = id

            sales_info.save()

            #update item Quantity
            item = Items.objects.get(item_code=item_code)
            Oty = int(item.item_quantity)-1

            #udate Item Level
            leve = int(item.item_level)+1

            Items.objects.filter(item_code=item_code).update(item_quantity=Oty, item_level=leve)

            return render(request,'salesmanapp/salesman.html')

        elif 'ireturn' in request.POST:
            item_code = request.POST['icode']
            salesman_name = request.POST['sale_man']

            item_id = Items.objects.get(item_code=item_code)
            shopname = item_id.shop_name

            return_info = Return(salesman=salesman_name,shop_name=shopname)

            item_id = Items.objects.get(item_code=item_code)
            id = item_id.id

            return_info.return_id_id = id

            return_info.save()

            #update item Quantity
            item = Items.objects.get(item_code=item_code)
            Oty = int(item.item_quantity)+1

            Items.objects.filter(item_code=item_code).update(item_quantity=Oty)
            return render(request,'salesmanapp/salesman.html')

    else:
        users = Account.objects.all()
        return render(request,'salesmanapp/salesman.html',{'users':users})

@login_required(login_url='login')
@admin_only
def sale_search_views(request):
    records = Sales.objects.all().order_by('-id')
    date_min = request.GET.get('strdate')
    date_max = request.GET.get('enddate')

    shop = request.GET.get('shop')
    sname = request.GET.get('sname')

    if date_min !="" and date_min is not None:
        records = records.filter(sale_date__gte = date_min)

    if date_max !="" and date_max is not None:
        records = records.filter(sale_date__lte = date_max)

    if sname !="" and sname is not None:
        records = records.filter(salesman__icontains = sname)

    if shop !="" and shop is not None:
        records = records.filter(shop_name__icontains = shop)

    return render(request,'salesmanapp/salesearch.html', {'records':records})

@login_required(login_url='login')
@admin_only
def sale_udate_views(request,id):
    if request.method == 'POST':
        saleprice = request.POST['sale_close']
        percent = int(saleprice) * 1/100

        Sales.objects.filter(id=id).update(sale_price=saleprice,comission=percent)
        messages.success(request,'sales updated successfully!')
        records = Sales.objects.all().order_by('-id')
        return render(request,'salesmanapp/salesearch.html', {'records':records})
    else:
        records = Sales.objects.get(id=id)
        return render(request,'salesmanapp/update.html',{'records':records})

@login_required(login_url='login')
@admin_only
def sale_delete_views(request,id):
    sales = Sales.objects.get(id=id)
    sales.delete()
    messages.success(request,'sales deleted successfully!')
    records = Sales.objects.all().order_by('-id')
    return render(request,'salesmanapp/salesearch.html', {'records':records})

@login_required(login_url='login')
@admin_only
def return_search_views(request):
    records = Return.objects.all().order_by('-id')
    date_min = request.GET.get('strdate')
    date_max = request.GET.get('enddate')

    shop = request.GET.get('shop')
    sname = request.GET.get('sname')

    if date_min !="" and date_min is not None:
        records = records.filter(return_date__gte = date_min)

    if date_max !="" and date_max is not None:
        records = records.filter(return_date__lte = date_max)

    if sname !="" and sname is not None:
        records = records.filter(salesman__icontains = sname)

    if shop !="" and shop is not None:
        records = records.filter(shop_name__icontains = shop)
    return render(request,'salesmanapp/return.html', {'records':records})

@login_required(login_url='login')
@admin_only
def sale_graph_views(request):
    labels = []
    data = []
    records = Sales.objects.all()
    for record in records:
        labels.append(record.sale_dt)
        data.append(record.sale_price)

    return render(request,'salesmanapp/salegraph.html',{'labels':labels, 'data':data})

@login_required(login_url='login')
#ajax call in barcode scaner
def get_iname_views(request):
    if request.method == "GET" and request.is_ajax():
        item_code = request.GET.get("itemname")
        try:
            idata = Items.objects.get(item_code = item_code)
        except:
            return JsonResponse({"success":False}, status=400)
        total_sale = int(idata.Open_stock) - int(idata.item_quantity)
        get_iname = {
               "item_id": idata.id,
               "shop_name": idata.shop_name,
               "item_name": idata.item_name,
               "brand_name": idata.brand_name,
               "item_size": idata.item_size,
               "item_color": idata.item_color,
               "item_unit": idata.item_unit,
               "item_quantity": idata.item_quantity,
               "Open_stock": idata.Open_stock,
               "total_sale": total_sale,
               "purchase_price": idata.purchase_price,
               "selling_price": idata.selling_price,
               "mrp": idata.mrp,
               "item_date": idata.item_date
        }
        return JsonResponse({"get_iname":get_iname}, status=200)
    return JsonResponse({"success":False}, status=400)
