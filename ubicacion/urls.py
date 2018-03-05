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
    url(r'^unidad/(?P<cod_sede>[\w]+)/(?P<cod_facultad>[\w]+)/$',
        views.UnidadDetailView.as_view(),
        name='unidad'),
    url(r'^seccion/(?P<cod_sede>[\w]+)/(?P<cod_facultad>[\w]+)/(?P<cod_escuela>[\w]+)/$',
        views.detalle_seccion, name='seccion'),
    url(
        r'^carrera/(?P<cod_sede>[\w]+)/(?P<cod_facultad>[\w]+)/(?P<cod_escuela>[\w]+)/(?P<cod_carrera>[\w]+)/$',
        views.CarreraDetailView.as_view(), name='carrera'),

    # Autocomplete
    url(r'^carrera-autocomplete/$', CarreraInstanciaAutocomplete.as_view(), name='carrera-autocomplete'),

    # Json
    url(r'^sedes/json/$', views.get_sedes, name='sedes-json'),
    url(r'^facultades/json/$', views.get_facultades, name='facultades-json'),
    url(r'^escuelas/json/$', views.get_escuelas, name='escuelas-json'),
    url(r'^departamentos/json/$', views.get_departamentos, name='escuelas-json'),
    url(r'^carreras/json/$', views.get_carreras, name='carreras-json'),
    # data-urls
    # Sedes
    url(r'^sede/(?P<sede_pk>[\w]+)/profesores/json/$', views.profesores_sede, name='profesores-sede'),
    url(r'^sede/(?P<sede_pk>[\w]+)/estudiantes/json/$', views.estudiantes_sede, name='estudiantes-sede'),
    # Facultades
    # Escuelas
    url(r'^escuela/(?P<escuela_pk>[\w+])/estudiantes/json/$', views.estudiantes_semestre_escuela,
        name='escuela-estudiantes'),
    url(r'^escuela/(?P<escuela_pk>[\w+])/proyecto/json/$', views.proyectos_semestre_escuela, name='escuela-proyectos'),
    url(r'^escuela/(?P<escuela_pk>[\w+])/anteproyecto/json/$', views.anteproyectos_semestre_escuela,
        name='escuela-anteproyectos'),
    # Departamento
    url(r'^departamento/(?P<departamento_pk>[\w+])/profesores/json/$', views.profesores_nivel,
        name='departamento-profesores'),
    url(r'^departamento/(?P<departamento_pk>[\w+])/actividades/json/$', views.actividades_tipo,
        name='departamento-actividades'),
    # Carreras
    url(r'^carrera/(?P<carrera_pk>[\w]+)/estudiantes/json/$', views.estudiantes_semestre_carrera,
        name='carrera-estudiantes'),
    url(r'^escuela/(?P<carrera_pk>[\w]+)/anteproyectos/json/$', views.anteproyectos_semestre_carrera,
        name='carrera-anteproyectos'),
    url(r'^escuela/(?P<carrera_pk>[\w]+)/proyectos/json/$', views.proyectos_semestre_carrera, name='carrera-proyectos'),
]
