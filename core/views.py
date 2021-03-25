from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import MedicalRecord


class HomeView(TemplateView):
    template_name = 'index.html'


class SimpleView(TemplateView):
    template_name = 'simple.html'

    def get_context_data(self, **kwargs):
        context = super(SimpleView, self).get_context_data(**kwargs)
        context['simple'] = MedicalRecord.objects.filter(type='simple')
        return context


class MedicationView(TemplateView):
    template_name = 'medication.html'

    def get_context_data(self, **kwargs):
        context = super(MedicationView, self).get_context_data(**kwargs)
        context['medication'] = MedicalRecord.objects.filter(type='medication')
        return context


class ObservationView(TemplateView):
    template_name = 'observation.html'

    def get_context_data(self, **kwargs):
        context = super(ObservationView, self).get_context_data(**kwargs)
        context['observation'] = MedicalRecord.objects.filter(type='observation')
        return context


class BandAidView(TemplateView):
    template_name = 'band_aid.html'

    def get_context_data(self, **kwargs):
        context = super(BandAidView, self).get_context_data(**kwargs)
        context['band_aid'] = MedicalRecord.objects.filter(type='band_aid')
        return context


class SutureView(TemplateView):
    template_name = 'suture.html'

    def get_context_data(self, **kwargs):
        context = super(SutureView, self).get_context_data(**kwargs)
        context['suture'] = MedicalRecord.objects.filter(type='suture')
        return context


class WithdrawalView(TemplateView):
    template_name = 'withdrawal.html'

    def get_context_data(self, **kwargs):
        context = super(WithdrawalView, self).get_context_data(**kwargs)
        context['withdrawal'] = MedicalRecord.objects.filter(type='withdrawal')
        return context


class RhView(TemplateView):
    template_name = 'rh.html'

    def get_context_data(self, **kwargs):
        context = super(RhView, self).get_context_data(**kwargs)
        context['rh'] = MedicalRecord.objects.filter(type='rh')
        return context


def search_view(request):
    context = {'qqq': 'q'}

    return render(request, 'search.html', context)
