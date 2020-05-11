import django_filters
from django_filters import DateFilter
from itemapp.models import *

class SaleFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='sale_date', lookup_expr='gte')
    end_date = DateFilter(field_name='sale_date', lookup_expr='lte')

    class Meta:
        model = Sales
        fields = '__all__'
        exclude = ['sales_id','item_code','salesman','mobile_number','sale_price',
                        'comission','exchange_item','return_item','sale_dt','sale_date']

class ReturnFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='return_date', lookup_expr='gte')
    end_date = DateFilter(field_name='return_date', lookup_expr='lte')

    class Meta:
        model = Return
        fields = '__all__'
        exclude = ['id','return_id','salesman','return_dt','return_date']
