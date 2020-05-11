from django.shortcuts import render
from .models import Items
from django.contrib import messages
import uuid
from django.http import JsonResponse
from .filters import ItemFilter
from django.contrib.auth.decorators import login_required
from loginapp.decorator import unauthenticated_user, allowed_user, admin_only

@login_required(login_url='login')
@admin_only
def dumpstock_views(request):
    if request.method == 'POST':
        id = request.POST['i_id']
        DumpQty = request.POST['DumpQty']

        Items.objects.filter(id=id).update(dump_stock=DumpQty)

        items = Items.objects.all()
        messages.success(request,'Dump Stock saved successfully!')
        return render(request,'itemapp/dumpstock.html',{'items':items})
    else:
        items = Items.objects.all()
        return render(request,'itemapp/dumpstock.html',{'items':items})


@login_required(login_url='login')
@admin_only
def items_views(request):
    return render(request,'itemapp/items.html')

@login_required(login_url='login')
@admin_only
def items_submit_views(request):
    if 'btn_save' in request.POST:
        itemname = request.POST['item_name']
        brandname = request.POST['brand_name']
        itemsize = request.POST['item_size']
        itemcolor = request.POST['item_color']
        itemunit = request.POST['item_unit']
        itemquantity = request.POST['item_quantity']
        purchaseprice = request.POST['purchase_price']
        # sellingprice = request.POST['selling_price']
        mrp = request.POST['mrp']
        item_date = request.POST['date']

        ucode = uuid.uuid4().hex[:10]
        ucode =  int(ucode, 16)
        itemcode = ucode

        amount = int(itemquantity) * int(purchaseprice)

        item_info = Items(item_name=itemname,brand_name=brandname,item_size=itemsize,
        item_color=itemcolor,item_unit=itemunit,item_quantity=itemquantity,Open_stock=itemquantity,purchase_price=purchaseprice,
        total_amount=amount,mrp=mrp,item_date=item_date,item_code=itemcode)

        item_info.save()
        messages.success(request,'Item saved successfully!')

        return render(request,'itemapp/items.html')
    elif 'btn_QR' in request.POST:
        itemname = request.POST['item_name']
        brandname = request.POST['brand_name']
        itemsize = request.POST['item_size']
        itemcolor = request.POST['item_color']
        itemunit = request.POST['item_unit']
        itemquantity = request.POST['item_quantity']
        purchaseprice = request.POST['purchase_price']
        # sellingprice = request.POST['selling_price']
        mrp = request.POST['mrp']
        item_date = request.POST['date']

        ucode = uuid.uuid4().hex[:10]
        ucode =  int(ucode, 16)
        itemcode = ucode

        amount = int(itemquantity) * int(purchaseprice)


        item_info = Items(item_name=itemname,brand_name=brandname,item_size=itemsize,
        item_color=itemcolor,item_unit=itemunit,item_quantity=itemquantity,Open_stock=itemquantity,purchase_price=purchaseprice,
        total_amount=amount,mrp=mrp,item_date=item_date,item_code=itemcode)

        item_info.save()
        id = item_info.id
        messages.success(request,'Item saved successfully now generate QRCode!')
        item = Items.objects.filter(id=id)
        return render(request,'itemapp/barcode.html',{'item':item})

@login_required(login_url='login')
@admin_only
def item_detail_views(request):
    item = Items.objects.all().order_by('id')
    return render(request,'itemapp/itemdetail.html',{'item':item})

@login_required(login_url='login')
@admin_only
def search_item_views(request):
    item = Items.objects.all()

    date_min = request.GET.get('strdate')
    date_max = request.GET.get('enddate')

    iname = request.GET.get('iname')
    bname = request.GET.get('bname')

    if date_min !="" and date_min is not None:
        item = item.filter(item_date__gte = date_min)

    if date_max !="" and date_max is not None:
        item = item.filter(item_date__lte = date_max)

    if iname !="" and iname is not None:
        item = item.filter(item_name__icontains = iname)

    if bname !="" and bname is not None:
        item = item.filter(brand_name__icontains = bname)


    return render(request,'itemapp/searchitem.html',{'item':item})

@login_required(login_url='login')
@admin_only
def restock_views(request):
    if request.method == 'POST':
        if 'btn_save' in request.POST:
            id = request.POST['item_id']
            itemquantity = request.POST['item_quantity']
            purchaseprice = request.POST['purchase_price']
            mrp = request.POST['mrp']
            item_date = request.POST['date']

            #update item Quantity
            item = Items.objects.get(id=id)
            Oty = int(item.item_quantity)+int(itemquantity)

            amount = int(Oty) * int(purchaseprice)


            Items.objects.filter(id=id).update(item_quantity=Oty, Open_stock=Oty, purchase_price=purchaseprice,
            mrp=mrp, total_amount=amount, item_date=item_date)

            items = Items.objects.all()
            messages.success(request,'Item saved successfully!')
            return render(request,'itemapp/restock.html',{'items':items})

        elif 'btn_QR' in request.POST:
            id = request.POST['item_id']
            itemquantity = request.POST['item_quantity']
            purchaseprice = request.POST['purchase_price']
            mrp = request.POST['mrp']
            item_date = request.POST['date']

            #update item Quantity
            item = Items.objects.get(id=id)
            Oty = int(item.item_quantity)+int(itemquantity)

            amount = int(Oty) * int(purchaseprice)


            Items.objects.filter(id=id).update(item_quantity=Oty, purchase_price=purchaseprice,
            mrp=mrp, total_amount=amount, item_date=item_date)

            messages.success(request,'Item saved successfully now generate QRCode!')
            item = Items.objects.filter(id=id)
            return render(request,'itemapp/barcode.html',{'item':item})

    else:
        items = Items.objects.all()
        return render(request,'itemapp/restock.html',{'items':items})


def getItemsInfo(request):
    if request.method == "GET" and request.is_ajax():
        id = request.GET.get("id")
        try:
            idata = Items.objects.get(id = id)
        except:
            return JsonResponse({"success":False}, status=400)

        item_info = {
        "item_id": idata.id,
        "item_name": idata.item_name,
        "brand_name": idata.brand_name,
        "item_size": idata.item_size,
        "item_color": idata.item_color,
        "item_unit": idata.item_unit,
        "item_quantity": idata.item_quantity,
        "purchase_price": idata.purchase_price,
        "selling_price": idata.selling_price,
        "mrp": idata.mrp,
        "item_date": idata.item_date
        }
        return JsonResponse({"item_info":item_info}, status=200)
    return JsonResponse({"success":False}, status=400)
