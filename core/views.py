from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView, FormView

from .models import MedicalRecord
from .forms import MedicalRecordModelForm


class HomeView(TemplateView):
    template_name = 'index.html'


class SimpleView(TemplateView):
    template_name = 'simple.html'

    def get_context_data(self, **kwargs):
        context = super(SimpleView, self).get_context_data(**kwargs)
        context['simple'] = MedicalRecord.objects.filter(type='simple')
        return context


class AddMedicalRecordView(FormView):
    template_name = 'add_medical_record.html'
    form_class = MedicalRecordModelForm
    success_url = reverse_lazy('index')

    def form_valid(self, form, *args, **kwargs):
        form.save()
        messages.success(self.request, 'Ficha cadastrada com sucesso.')
        return super(AddMedicalRecordView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao cadastrar imagem.')
        return super(AddMedicalRecordView, self).form_invalid(form, *args, **kwargs)


def search_view(request):
    context = {}
    medical_record = None
    name = sus = type = ''
    birth_date = consultation_date = '1111-11-11'

    if request.method == 'GET':
        if request.GET.get('name'):
            name = request.GET.get('name')
        if request.GET.get('sus'):
            sus = request.GET.get('sus')
        if request.GET.get('birth_date'):
            birth_date = request.GET.get('birth_date')
        if request.GET.get('consultation_date'):
            consultation_date = request.GET.get('consultation_date')
        type = request.GET.get('type')

        if name != '' and sus != '' and birth_date != '1111-11-11' and consultation_date != '1111-11-11':
            if type != 'all':
                medical_record = MedicalRecord.objects.filter(
                    name=name,
                    sus=sus,
                    birth_date=birth_date,
                    consultation_date=consultation_date,
                    type=type
                )
            else:
                medical_record = MedicalRecord.objects.filter(
                    name=name,
                    sus=sus,
                    birth_date=birth_date,
                    consultation_date=consultation_date
                )

        elif name != '' and sus != '' and birth_date != '1111-11-11':
            if type != 'all':
                medical_record = MedicalRecord.objects.filter(
                    name=name,
                    sus=sus,
                    birth_date=birth_date,
                    type=type
                )
            else:
                medical_record = MedicalRecord.objects.filter(name=name, sus=sus, birth_date=birth_date)

        elif name != '' and sus != '' and consultation_date != '1111-11-11':
            if type != 'all':
                medical_record = MedicalRecord.objects.filter(
                    name=name,
                    sus=sus,
                    consultation_date=consultation_date,
                    type=type
                )
            else:
                medical_record = MedicalRecord.objects.filter(name=name, sus=sus, birth_date=birth_date)

        elif name != '' and birth_date != '1111-11-11' and consultation_date != '1111-11-11':
            if type != 'all':
                medical_record = MedicalRecord.objects.filter(
                    name=name,
                    birth_date=birth_date,
                    consultation_date=consultation_date,
                    type=type
                )
            else:
                medical_record = MedicalRecord.objects.filter(
                    name=name,
                    birth_date=birth_date,
                    consultation_date=consultation_date
                )

        elif name != '' and sus != '':
            if type != 'all':
                medical_record = MedicalRecord.objects.filter(name=name, sus=sus, type=type)
            else:
                medical_record = MedicalRecord.objects.filter(name=name, sus=sus)

        elif name != '' and birth_date != '1111-11-11':
            if type != 'all':
                medical_record = MedicalRecord.objects.filter(name=name, birth_date=birth_date, type=type)
            else:
                medical_record = MedicalRecord.objects.filter(name=name, birth_date=birth_date)

        elif name != '' and consultation_date != '1111-11-11':
            if type != 'all':
                medical_record = MedicalRecord.objects.filter(
                    name=name,
                    consultation_date=consultation_date,
                    type=type
                )
            else:
                medical_record = MedicalRecord.objects.filter(name=name, consultation_date=consultation_date)

        elif sus != '' and birth_date != '1111-11-11' and consultation_date != '1111-11-11':
            if type != 'all':
                medical_record = MedicalRecord.objects.filter(
                    sus=sus,
                    birth_date=birth_date,
                    consultation_date=consultation_date,
                    type=type
                )
            else:
                medical_record = MedicalRecord.objects.filter(
                    sus=sus,
                    birth_date=birth_date,
                    consultation_date=consultation_date
                )

        elif sus != '' and birth_date != '1111-11-11':
            if type != 'all':
                medical_record = MedicalRecord.objects.filter(sus=sus, birth_date=birth_date, type=type)
            else:
                medical_record = MedicalRecord.objects.filter(sus=sus, birth_date=birth_date)

        elif sus != '' and consultation_date != '1111-11-11':
            if type != 'all':
                medical_record = MedicalRecord.objects.filter(
                    sus=sus,
                    consultation_date=consultation_date,
                    type=type
                )
            else:
                medical_record = MedicalRecord.objects.filter(sus=sus, consultation_date=consultation_date)

        elif birth_date != '1111-11-11' and consultation_date != '1111-11-11':
            if type != 'all':
                medical_record = MedicalRecord.objects.filter(
                    birth_date=birth_date,
                    consultation_date=consultation_date,
                    type=type
                )
            else:
                medical_record = MedicalRecord.objects.filter(
                    birth_date=birth_date,
                    consultation_date=consultation_date
                )

        elif name != '':
            if type != 'all':
                medical_record = MedicalRecord.objects.filter(name=name, type=type)
            else:
                medical_record = MedicalRecord.objects.filter(name=name)

        elif sus != '':
            if type != 'all':
                medical_record = MedicalRecord.objects.filter(sus=sus, type=type)
            else:
                medical_record = MedicalRecord.objects.filter(birth_date=birth_date)

        elif birth_date != '1111-11-11':
            if type != 'all':
                medical_record = MedicalRecord.objects.filter(birth_date=birth_date, type=type)
            else:
                medical_record = MedicalRecord.objects.filter(birth_date=birth_date)

        elif consultation_date != '1111-11-11':
            if type != 'all':
                medical_record = MedicalRecord.objects.filter(consultation_date=consultation_date, type=type)
            else:
                medical_record = MedicalRecord.objects.filter(consultation_date=consultation_date)

        elif type != 'all':
            medical_record = MedicalRecord.objects.filter(type=type)

        context = {'medical_record': medical_record}

    return render(request, 'search.html', context)
