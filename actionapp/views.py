from django.shortcuts import render
from itemapp.models import Items
from django.contrib import messages

# Create your views here.
def item_update_views(request, id):
    item = Items.objects.filter(id=id)
    return render(request,'actionapp/upitem.html',{'item':item})

def item_edit_views(request):
    if request.method == 'POST':
        itemid = request.POST['item_id']
        itemname = request.POST['item_name']
        brandname = request.POST['brand_name']
        itemsize = request.POST['item_size']
        itemcolor = request.POST['item_color']
        itemunit = request.POST['item_unit']
        itemquantity = request.POST['item_quantity']
        purchaseprice = request.POST['purchase_price']
        sellingprice = request.POST['selling_price']
        mrp = request.POST['mrp']

        Items.objects.filter(id=itemid).update(item_name=itemname,
        brand_name=brandname, item_size=itemsize, item_color=itemcolor,
        item_unit=itemunit, item_quantity=itemquantity,Open_stock=itemquantity, purchase_price=purchaseprice,
        selling_price=sellingprice, mrp=mrp)

        messages.success(request,'Item update successfully!')
        return render(request,'actionapp/upitem.html')

def item_delete_views(request, id):
    item = Items.objects.get(id=id)
    item.delete()
    messages.success(request,'Item deleted successfully!')
    item = Items.objects.all().order_by('-id')
    return render(request,'itemapp/itemdetail.html',{'item':item})
