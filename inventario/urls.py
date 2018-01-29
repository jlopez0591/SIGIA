from django.conf.urls import url

from inventario.autocomplete import CategoriaAutocomplete, FabricanteAutocomplete, ModeloAutocomplete, AulaAutocomplete
from inventario.models import Aula
from inventario.views import CategoriaCreateView, CategoriaListView, CategoriaDetailView, FabricanteCreateView, \
    FabricanteDetailView, EquipoCreateView, EquipoListView, \
    FabricanteListView, ModeloCreateView, ModeloListView, ModeloDetailView, AulaListView, AulaCreateView, \
    AulaDetailView, AulaUpdateView, ModeloUpdateView, EquipoDetailView, EquipoUpdateView

from . import views

app_name = 'inventario'
urlpatterns = [
    # CRUD Categoria
    url(r'^categorias/$', CategoriaListView.as_view(), name='categoria-lista'),
    url(r'^categoria/crear/$', CategoriaCreateView.as_view(), name='crear-categoria'),
    url(r'^categoria/(?P<pk>[\d+])/$', CategoriaDetailView.as_view(), name='categoria-detalle'),
    # CRUD Fabricante
    url(r'^fabricantes/$', FabricanteListView.as_view(), name='fabricante-lista'),
    url(r'^fabricantes/crear/$', FabricanteCreateView.as_view(), name='crear-fabricante'),
    url(r'^fabricante/(?P<pk>[\d+])/$', FabricanteDetailView.as_view(), name='fabricante-detalle'),
    # CRUD Modelo
    url(r'^modelos/$', ModeloListView.as_view(), name='modelo-lista'),
    url(r'^modelo/crear/$', ModeloCreateView.as_view(), name='crear-modelo'),
    url(r'^modelo/(?P<pk>[\d+])/$', ModeloDetailView.as_view(), name='modelo-detalle'),
    url(r'^modelo/(?P<pk>[\d+])/editar/$', ModeloUpdateView.as_view(), name='modelo-modificar'),
    # CRUD Equipo
    url(r'^equipos/$', EquipoListView.as_view(), name='lista-equipo'),
    url(r'^equipo/crear/$', EquipoCreateView.as_view(), name='crear-equipo'),
    url(r'^equipo/(?P<pk>[\d+])/$', EquipoDetailView.as_view(), name='detalle-equipo'),
    url(r'^equipo/(?P<pk>[\d+])/editar$', EquipoUpdateView.as_view(), name='editar-equipo'),
    # CRUD Aula
    url(r'^aulas/$', AulaListView.as_view(), name='lista-aulas'),
    url(r'^aula/(?P<pk>[\d+])/$', AulaDetailView.as_view(), name='detalle-aulas'),
    url(r'^aulas/crear$', AulaCreateView.as_view(), name='crear-aulas'),
    url(r'^aula/(?P<pk>[\d+])/editar/$', AulaUpdateView.as_view(), name='editar-aulas'),
    # Autocompletes
    url(r'^categoria-autocomplete/$', CategoriaAutocomplete.as_view(), name='categoria-autocomplete'),
    url(r'^fabricante-autocomplete/$', FabricanteAutocomplete.as_view(), name='fabricante-autocomplete'),
    url(r'^modelo-autocomplete/$', ModeloAutocomplete.as_view(), name='modelo-autocomplete'),
    url(r'^aula-autocomplete/$', AulaAutocomplete.as_view(), name='aula-autocomplete'),
    # url(r'^modelo-autocomplete/$', ModeloAutocomplete.as_view(), name='modelo-autocomplete'),
    # JSON
    url(r'^categorias/json/$', views.categorias_json, name='categoria-json'),
    url(r'^fabricantes/json/$', views.fabricantes_json, name='categoria-json'),
    url(r'^modelos/json/$', views.modelos_json, name='categoria-json'),
    url(r'^aulas/json/$', views.aulas_json, name='categoria-json'),
    url(r'^equipos/json/$', views.equipos_json, name='categoria-json'),
]
