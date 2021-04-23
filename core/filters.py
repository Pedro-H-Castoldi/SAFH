import django_filters

from .models import MedicalRecord


class MedicalRecordFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Nome', lookup_expr='icontains')
    sus = django_filters.CharFilter(label='SUS', lookup_expr='icontains')
    birth_date = django_filters.DateFilter(label='Data Nascimento', lookup_expr='icontains')
    consultation_date = django_filters.DateFilter(label='Date Consulta', lookup_expr='exact')
    type = django_filters.CharFilter(label='Tipo', lookup_expr='icontains')

    class Meta:
        model = MedicalRecord
        fields = ('name', 'sus', 'birth_date', 'consultation_date', 'type')


