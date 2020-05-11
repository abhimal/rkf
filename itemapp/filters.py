import django_filters
from django_filters import DateFilter
from .models import *

class ItemFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='item_date', lookup_expr='gte')
    end_date = DateFilter(field_name='item_date', lookup_expr='lte')
    class Meta:
        model = Items
        fields = '__all__'
        exclude = ['item_size','item_color','item_unit','item_quantity','Open_stock','purchase_price',
        'selling_price','mrp','item_code','item_date','total_amount','item_level']
