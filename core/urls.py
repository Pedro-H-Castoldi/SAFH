from django.urls import path

from .views import (HomeView, SimpleView, AddMedicalRecordView, search_view, MedicalRecordView, EditMedicalRecord, DeleteMedicalRecord)

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('simples/', SimpleView.as_view(), name='simple'),
    path('cadastrar-fichas', AddMedicalRecordView.as_view(), name='add_record'),
    path('busca/', search_view, name='search'),
    path('busca/<int:pk>', MedicalRecordView.as_view(), name='medical_record'),
    path('<int:pk>/update/', EditMedicalRecord.as_view(), name='edit_medical_record'),
    path('<int:pk>/delete/', DeleteMedicalRecord.as_view(), name='delete_medical_record')
]