from django_filters import rest_framework as filters
from .models import Monografia

class MonografiaFilter(filters.FilterSet):
    data_defesa = filters.DateFilter(field_name='data_defesa', lookup_expr='exact')

    class Meta:
        model = Monografia
        fields = {
            'data_defesa': ['exact']
        }