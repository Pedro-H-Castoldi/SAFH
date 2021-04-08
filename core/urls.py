from django.urls import path

from .views import (HomeView, SimpleView, AddMedicalRecordView, search_view)

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('simples/', SimpleView.as_view(), name='simple'),
    path('cadastrar-fichas', AddMedicalRecordView.as_view(), name='add_record'),
    path('search/', search_view, name='search')
]