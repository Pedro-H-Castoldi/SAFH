from django.contrib import admin
from .models import MedicalRecord


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):

    list_display =('type', 'name', 'sus', 'sex', 'birth_date', 'consultation_date')
