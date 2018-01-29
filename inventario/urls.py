from django.conf.urls import url
from inventario.autocomplete import CategoriaAutocomplete, FabricanteAutocomplete, ModeloAutocomplete, AulaAutocomplete
from inventario.views import aula, categoria, equipo, fabricante, modelo, transferencia

app_name = 'inventario'
urlpatterns = [
    # CRUD Categoria
    url(r'^categorias/$', categoria.CategoriaListView.as_view(), name='categoria-lista'),
    url(r'^categoria/crear/$', categoria.CategoriaCreateView.as_view(), name='crear-categoria'),
    url(r'^categoria/(?P<pk>[\d+])/$', categoria.CategoriaDetailView.as_view(), name='categoria-detalle'),
    # CRUD Fabricante
    url(r'^fabricantes/$', fabricante.FabricanteListView.as_view(), name='fabricante-lista'),
    url(r'^fabricantes/crear/$', fabricante.FabricanteCreateView.as_view(), name='crear-fabricante'),
    url(r'^fabricante/(?P<pk>[\d+])/$', fabricante.FabricanteDetailView.as_view(), name='fabricante-detalle'),
    # CRUD Modelo
    url(r'^modelos/$', modelo.ModeloListView.as_view(), name='modelo-lista'),
    url(r'^modelo/crear/$', modelo.ModeloCreateView.as_view(), name='crear-modelo'),
    url(r'^modelo/(?P<pk>[\d+])/$', modelo.ModeloDetailView.as_view(), name='modelo-detalle'),
    url(r'^modelo/(?P<pk>[\d+])/editar/$', modelo.ModeloUpdateView.as_view(), name='modelo-modificar'),
    # CRUD Equipo
    url(r'^equipos/$', equipo.EquipoListView.as_view(), name='lista-equipo'),
    url(r'^equipos/(?P<pk>[\d+])/lista/$', equipo.EquipoFacultadListView.as_view(), name='facultad-equipo'),
    url(r'^equipo/crear/$', equipo.EquipoCreateView.as_view(), name='crear-equipo'),
    url(r'^equipo/(?P<pk>[\d+])/$', equipo.EquipoDetailView.as_view(), name='detalle-equipo'),
    url(r'^equipo/(?P<pk>[\d+])/editar$', equipo.EquipoUpdateView.as_view(), name='editar-equipo'),
    # CRUD Aula
    url(r'^aulas/$', aula.AulaListView.as_view(), name='lista-aulas'),
    url(r'^aulas/(?P<pk>[\d+])/lista/$', aula.AulaFacultadListView.as_view(), name='facultad-aulas'),
    url(r'^aula/(?P<pk>[\d+])/$', aula.AulaDetailView.as_view(), name='detalle-aulas'),
    url(r'^aulas/crear$', aula.AulaCreateView.as_view(), name='crear-aulas'),
    url(r'^aula/(?P<pk>[\d+])/editar/$', aula.AulaUpdateView.as_view(), name='editar-aulas'),
    # Autocompletes
    url(r'^categoria-autocomplete/$', CategoriaAutocomplete.as_view(), name='categoria-autocomplete'),
    url(r'^fabricante-autocomplete/$', FabricanteAutocomplete.as_view(), name='fabricante-autocomplete'),
    url(r'^modelo-autocomplete/$', ModeloAutocomplete.as_view(), name='modelo-autocomplete'),
    url(r'^aula-autocomplete/$', AulaAutocomplete.as_view(), name='aula-autocomplete'),
    # JSON
    url(r'^categorias/json/$', transferencia.categorias_json, name='categoria-json'),
    url(r'^fabricantes/json/$', transferencia.fabricantes_json, name='categoria-json'),
    url(r'^modelos/json/$', transferencia.modelos_json, name='categoria-json'),
    url(r'^aulas/json/$', transferencia.aulas_json, name='categoria-json'),
    url(r'^equipos/json/$', transferencia.equipos_json, name='categoria-json'),
]
