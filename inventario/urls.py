from django.conf.urls import url

from inventario.autocomplete import CategoriaAutocomplete, FabricanteAutocomplete, ModeloAutocomplete
from inventario.views import CategoriaCreateView, CategoriaListView, CategoriaDetailView, FabricanteCreateView, \
    FabricanteDetailView, EquipoCreateView, EquipoListView, \
    FabricanteListView, ModeloCreateView, ModeloListView, ModeloDetailView

from inventario import views

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
    # CRUD Equipo
    url(r'^equipos/$', EquipoListView.as_view(), name='lista-equipo'),
    url(r'^equipo/crear/$', EquipoCreateView.as_view(), name='crear-equipo'),
    url(r'^equipo/(?P<pk>[\d+])/$', ModeloCreateView.as_view(), name='detalle-equipo'),
    url(r'^equipo/(?P<pk>[\d+])/editar$', EquipoCreateView.as_view(), name='detalle-equipo'),

    # Carga Masiva
    url(r'^fabricante/carga/$', views.carga_fabricantes, name='carga-fabricantes'),
    url(r'^categoria/carga/$', views.carga_categorias, name='carga-categoria'),
    url(r'^modelos/carga/$', views.carga_modelos, name='carga-modelos'),

    # JSONs

    # Autocompletes
    url(r'^categoria-autocomplete/$', CategoriaAutocomplete.as_view(), name='categoria-autocomplete'),
    url(r'^fabricante-autocomplete/$', FabricanteAutocomplete.as_view(), name='fabricante-autocomplete'),
    url(r'^modelo-autocomplete/$', ModeloAutocomplete.as_view(), name='modelo-autocomplete'),

]
