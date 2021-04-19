import django_filters

from .models import MedicalRecord

class MedicalRecordFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    sus = django_filters.CharFilter(lookup_expr='icontains')
    birth_date = django_filters.CharFilter(lookup_expr='icontains')
    consultation_date = django_filters.CharFilter(lookup_expr='incontains')
    type = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = MedicalRecord
        fields = ('name', 'sus', 'birth_date', 'consultation_date', 'type')


