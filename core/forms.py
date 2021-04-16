from django import forms

from .models import MedicalRecord
from .admin import MedicalRecordAdmin

class DateInput(forms.DateInput):
    input_type = 'date'


class MedicalRecordModelForm(forms.ModelForm):

    class Meta:
        model = MedicalRecord
        fields = ['name', 'sus', 'sex', 'birth_date', 'consultation_date', 'medical_record', 'type']
        widgets = {
            'birth_date': DateInput(),
            'consultation_date': DateInput()
        }


