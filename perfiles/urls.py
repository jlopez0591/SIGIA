from django.conf.urls import url
from perfiles.views import *
from perfiles import views
from .views import ProfesoresAutocomplete

app_name = 'perfil'
urlpatterns = [
    url(r'^$', PerfilDetailView.as_view(), name='ver'),
    url(r'^editar/$', PerfilUpdateView.as_view(), name='editar'),
    url(r'^(?P<pk>[0-9]+)/$', PerfilPublicoView.as_view(), name='publico'),
    url(r'^lista/$', views.consulta_profesor, name='lista'),

    # Autocompletado
    url(r'^autocomplete/$', ProfesoresAutocomplete.as_view(), name='autocomplete'),
]
