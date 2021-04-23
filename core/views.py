from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic import TemplateView, DeleteView, UpdateView, CreateView

from .models import MedicalRecord
from .forms import MedicalRecordModelForm
from .filters import MedicalRecordFilter


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        object_list = MedicalRecord.objects.all()
        medical_record_list = MedicalRecordFilter(self.request.GET, queryset=object_list)
        context['object_list'] = object_list
        context['filter'] = medical_record_list

        return context


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class DeleteMedicalRecord(DeleteView):
    template_name = 'delete_medical_record.html'

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(MedicalRecord, id=id_)

    def get_success_url(self):
        return reverse('index')


@method_decorator(login_required, name='dispatch')
class MedicalRecordView(TemplateView):
    template_name = 'details_medical_record.html'

    def get_context_data(self, **kwargs):
        context = super(MedicalRecordView, self).get_context_data(**kwargs)
        context['medical_record'] = MedicalRecord.objects.filter(id=kwargs.get('pk'))
        return context


@method_decorator(login_required, name='dispatch')
class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        if self.request.GET['name'] == self.request.GET['sus'] == self.request.GET['birth_date'] == self.request.GET['consultation_date'] == self.request.GET['type'] == '':
            return

        context = super(SearchView, self).get_context_data(**kwargs)
        object_list = MedicalRecord.objects.all()
        medical_record_list = MedicalRecordFilter(self.request.GET, queryset=object_list)
        context['object_list'] = object_list
        context['filter'] = medical_record_list
        return context

