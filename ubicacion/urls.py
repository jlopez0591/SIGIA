from django.conf.urls import url
from . import views
from .views import CarreraInstanciaAutocomplete

app_name = 'ubicacion'
urlpatterns = [
    # Consultas
    url(r'^sedes/$', views.consulta_sede, name='sedes'),
    url(r'^unidades/$', views.consulta_unidad, name='unidades'),
    url(r'^secciones/$', views.consulta_seccion, name='secciones'),
    url(r'^carreras/$', views.consulta_carrera, name='carreras'),

    # Detalle
    url(r'^sede/(?P<cod_sede>[\w]+)/$', views.SedeDetailView.as_view(),
        name='sede'),
    url(r'^unidad/(?P<cod_sede>[\w]+)/(?P<cod_unidad>[\w]+)/$',
        views.UnidadDetailView.as_view(),
        name='unidad'),
    url(r'^seccion/(?P<cod_sede>[\w]+)/(?P<cod_unidad>[\w]+)/(?P<cod_seccion>[\w]+)/$',
        views.SeccionDetailView.as_view(), name='seccion'),
    url(
        r'^carrera/(?P<cod_sede>[\w]+)/(?P<cod_unidad>[\w]+)/(?P<cod_seccion>[\w]+)/(?P<cod_carrera>[\w]+)/$',
        views.CarreraDetailView.as_view(), name='carrera'),

    # Autocomplete
    url(r'^carrera-autocomplete/$', CarreraInstanciaAutocomplete.as_view(), name='carrera-autocomplete'),

    # Json
    url(r'^sedes/json/$', views.get_sedes, name='sedes-json'),
    url(r'^facultades/json/$', views.get_facultades, name='facultades-json'),
    url(r'^escuelas/json/$', views.get_escuelas, name='escuelas-json'),
    url(r'^departamentos/json/$', views.get_departamentos, name='escuelas-json'),
    url(r'^carreras/json/$', views.get_carreras, name='carreras-json'),
    # Instancias JSON
    # url(r'^carreras/json/$', views.get_carreras, name='carreras-json'),
    # url(r'^carreras/json/$', views.get_carreras, name='carreras-json'),
    # url(r'^carreras/json/$', views.get_carreras, name='carreras-json'),
    # url(r'^carreras/json/$', views.get_carreras, name='carreras-json'),
]
