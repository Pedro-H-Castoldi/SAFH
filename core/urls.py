from django.urls import path

from .views import (HomeView,
                    SimpleView,
                    MedicationView,
                    ObservationView,
                    SutureView,
                    BandAidView,
                    WithdrawalView,
                    RhView,
                    search_view)

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('simples/', SimpleView.as_view(), name='simple'),
    path('medicacao/', MedicationView.as_view(), name='medication'),
    path('observacao/', ObservationView.as_view(), name='observation'),
    path('sutura/', SutureView.as_view(), name='suture'),
    path('curativo/', BandAidView.as_view(), name='band_aid'),
    path('retirada_de_pontos/', WithdrawalView.as_view(), name='withdrawal'),
    path('rh/', RhView.as_view(), name='rh'),
    path('search/', search_view, name='search')
]