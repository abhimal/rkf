from django.db import models
import datetime

# Create your models here.
class Items(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=64)
    brand_name = models.CharField(max_length=64)
    item_size =  models.CharField(max_length=64)
    item_color = models.CharField(max_length=64)
    item_unit =  models.CharField(max_length=64)
    item_quantity = models.IntegerField()
    Open_stock = models.IntegerField(default='0')
    dump_stock = models.IntegerField(default='0')
    purchase_price = models.FloatField()
    total_amount = models.FloatField()
    selling_price =  models.FloatField(default="0.0")
    mrp = models.FloatField()
    item_code = models.CharField(max_length=64)
    item_level = models.IntegerField(default='0')
    item_date = models.DateField()

    def __str__(self):#show tabel name on admin
        return self.item_name

class Sales(models.Model):
    sales_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    item_code = models.CharField(max_length=64)
    salesman =  models.CharField(max_length=64)
    mobile_number = models.CharField(max_length=64)
    sale_price = models.FloatField()
    comission = models.FloatField()
    exchange_item = models.BooleanField(default=False)
    return_item = models.CharField(max_length=64)
    sale_dt = models.DateTimeField(auto_now_add=True)
    sale_date = models.DateField(auto_now_add=True)

    def __str__(self):#show tabel name on admin
        return self.salesman

class Return(models.Model):
    return_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    salesman =  models.CharField(max_length=64)
    return_dt = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField(auto_now_add=True)

    def __str__(self):#show tabel name on admin
        return self.return_id

class StockAudit(models.Model):
    stock_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    opening_stock =  models.IntegerField(default='0')
    closing_stock =  models.IntegerField(default='0')
    physical_qty =  models.IntegerField()
    total_sale =  models.IntegerField(default='0')
    missing_qty =  models.IntegerField(default='0')
    stock_dt = models.DateTimeField(auto_now_add=True)
    stock_audit_date = models.DateField(auto_now_add=True)

    def __str__(self):#show tabel name on admin
        return self.stock_id
