from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic import TemplateView, FormView, DeleteView, UpdateView, CreateView

from .models import MedicalRecord
from .forms import MedicalRecordModelForm
from .filters import MedicalRecordFilter


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        object_list = MedicalRecord.objects.all()
        medical_record_list = MedicalRecordFilter(self.request.GET, queryset=object_list)
        context['object_list'] = object_list
        context['filter'] = medical_record_list

        return context



class AddMedicalRecordView(CreateView):
    template_name = 'add_medical_record.html'
    form_class = MedicalRecordModelForm
    success_url = reverse_lazy('add_record')

    def form_valid(self, form, *args, **kwargs):
        form.save()
        messages.success(self.request, 'Ficha cadastrada com sucesso.')
        return super(AddMedicalRecordView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao cadastrar imagem.')
        return super(AddMedicalRecordView, self).form_invalid(form, *args, **kwargs)


class EditMedicalRecord(UpdateView):
    template_name = 'add_medical_record.html'
    form_class = MedicalRecordModelForm

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(MedicalRecord, id=id_)

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Ficha médica editada com sucesso')
        return super(EditMedicalRecord, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao editar ficha. Preencha o formulário corretamente')
        return super(EditMedicalRecord, self).form_invalid(form, *args, **kwargs)


class DeleteMedicalRecord(DeleteView):
    template_name = 'delete_medical_record.html'

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(MedicalRecord, id=id_)

    def get_success_url(self):
        return reverse('index')


class MedicalRecordView(TemplateView):
    template_name = 'details_medical_record.html'

    def get_context_data(self, **kwargs):
        context = super(MedicalRecordView, self).get_context_data(**kwargs)
        context['medical_record'] = MedicalRecord.objects.filter(id=kwargs.get('pk'))
        return context


def search_view(request):
    object_list = MedicalRecord.objects.all()
    medical_record_list = MedicalRecordFilter(request.GET, queryset=object_list)
    context = {
        'object_list': object_list,
        'filter': medical_record_list
    }

    return render(request, 'search.html', context)




"""
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

"""