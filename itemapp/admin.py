from django.contrib import admin
from itemapp.models import Items
from itemapp.models import Sales
from itemapp.models import Return
from itemapp.models import StockAudit

# Register your models here.
class ItemsAdmin(admin.ModelAdmin):
    list_display = ['id','item_name','brand_name','item_size','item_color',
                   'item_unit','item_quantity','Open_stock','purchase_price','total_amount','selling_price',
                    'mrp','item_date','item_code','item_level']

class SalesAdmin(admin.ModelAdmin):
    list_display = ['id','sales_id','item_code','salesman','mobile_number','sale_price',
                    'comission','exchange_item','return_item','sale_dt','sale_date']

class ReturnAdmin(admin.ModelAdmin):
    list_display = ['id','return_id','salesman','return_dt','return_date']

class StockAdmin(admin.ModelAdmin):
    list_display = ['id','stock_id','opening_stock','closing_stock','physical_qty','total_sale','missing_qty','stock_dt','stock_audit_date']

admin.site.register(Items, ItemsAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(Return, ReturnAdmin)
admin.site.register(StockAudit, StockAdmin)
