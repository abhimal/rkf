from django.shortcuts import render
from django.views import View
from itemapp.models import Items, StockAudit
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from loginapp.decorator import unauthenticated_user, allowed_user, admin_only
from django.utils.datastructures import MultiValueDictKeyError
from .filters import StockFilter
from .render import Render
# Create your views here.

class Pdf(View):
    def get(self, request):
        records = StockAudit.objects.all()
        params = {
            'records': records,
            'request': request
        }
        return Render.render('stockapp/pdf.html', params)

@login_required(login_url='login')
@admin_only
def stockaudit_views(request):
    if request.method == 'POST':
        item_code = request.POST['icode']
        qty = request.POST['head_qty']

        item_id = Items.objects.get(item_code=item_code)

        id = item_id.id
        Open_stock = item_id.Open_stock
        Closing_stock = item_id.item_quantity
        shop = item_id.shop_name

        total_sale = int(Open_stock) - int(Closing_stock)
        missing_item = int(Closing_stock) - int(qty)

        stock_info = StockAudit(opening_stock=Open_stock,closing_stock=Closing_stock,physical_qty=qty, total_sale=total_sale, missing_qty=missing_item, shop_name=shop)

        stock_info.stock_id_id = id

        stock_info.save()

        return render(request,'stockapp/stockaudit.html')
    else:
        return render(request,'stockapp/stockaudit.html')

@login_required(login_url='login')
@admin_only
def stock_report_views(request):
    records = StockAudit.objects.all().order_by('-id')
    shop = request.GET.get('shop')
    date_min = request.GET.get('strdate')
    date_max = request.GET.get('enddate')

    if shop !="" and shop is not None:
        records = records.filter(shop_name__icontains = shop)

    if date_min !="" and date_min is not None:
        records = records.filter(stock_audit_date__gte = date_min)

    if date_max !="" and date_max is not None:
        records = records.filter(stock_audit_date__lte = date_max)

    return render(request,'stockapp/stockreport.html', {'records':records})
