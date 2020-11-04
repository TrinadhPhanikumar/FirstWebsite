import django_filters
from home.models import *

class ListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model=List
        fields=['name']
