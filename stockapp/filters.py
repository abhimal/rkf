import django_filters
from django_filters import DateFilter
from itemapp.models import *

class StockFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='stock_audit_date', lookup_expr='gte')
    end_date = DateFilter(field_name='stock_audit_date', lookup_expr='lte')

    class Meta:
        model = StockAudit
        fields = '__all__'
        exclude = ['stock_id','physical_qty','opening_stock','closing_stock','total_sale','missing_qty','stock_dt',
                        'stock_audit_date']
