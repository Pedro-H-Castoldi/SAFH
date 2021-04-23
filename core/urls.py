from django.urls import path

from .views import (HomeView, AddMedicalRecordView, SearchView, MedicalRecordView, EditMedicalRecord, DeleteMedicalRecord)

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('cadastrar-fichas', AddMedicalRecordView.as_view(), name='add_record'),
    path('busca/', SearchView.as_view(), name='search'),
    path('busca/<int:pk>', MedicalRecordView.as_view(), name='medical_record'),
    path('<int:pk>/update/', EditMedicalRecord.as_view(), name='edit_medical_record'),
    path('<int:pk>/delete/', DeleteMedicalRecord.as_view(), name='delete_medical_record')
]