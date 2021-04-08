from django import forms

from .models import MedicalRecord
from .admin import MedicalRecordAdmin


class MedicalRecordModelForm(forms.ModelForm):

    class Meta:
        model = MedicalRecord
        fields = ['name', 'sus', 'sex', 'birth_date', 'consultation_date', 'medical_record', 'type']


