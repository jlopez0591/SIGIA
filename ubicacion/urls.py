from django.conf.urls import url
from . import views
from ubicacion.views import SedeListView, FacultadInstanciaListView, EscuelaInstanciaListView, CarreraInstanciaListView, \
    DepartamentoInstanciaListView
from ubicacion.views import SedeDetailView, FacultadInstanciaDetailView, EscuelaInstanciaDetailView, \
    DepartamentoInstanciaDetailView, CarreraInstanciaDetailView
from .views import CarreraInstanciaAutocomplete

app_name = 'ubicacion'
urlpatterns = [
    # Consultas v1
    # url(r'^sedes/$', views.consulta_sede, name='sedes'),
    # url(r'^unidades/$', views.consulta_unidad, name='unidades'),
    # url(r'^secciones/$', views.consulta_seccion, name='secciones'),
    # url(r'^carreras/$', views.consulta_carrera, name='carreras'),

    # Detalle v1
    # url(r'^sede/(?P<pk>[\w]+)/$', views.SedeDetailView.as_view(), name='sede'),
    # url(r'^facultad/(?P<pk>[\w]+)$', views.UnidadDetailView.as_view(), name='unidad'),
    # url(r'^seccion/(?P<pk>[\w]+)/$', views.detalle_seccion, name='seccion'),
    # url(r'^carrera/(?P<pk>[\w]+)/$', views.CarreraDetailView.as_view(), name='carrera'),

    # Consultas v2
    url(r'^sedes/$', SedeListView.as_view(), name='sedes'),
    url(r'^facultades/$', FacultadInstanciaListView.as_view(), name='facultades'),
    url(r'^escuelas/$', EscuelaInstanciaListView.as_view(), name='escuelas'),
    url(r'^departamentos/$', DepartamentoInstanciaListView.as_view(), name='departamentos'),
    url(r'^carreras/$', CarreraInstanciaListView.as_view(), name='carreras'),

    # Detalle v2
    url(r'^sede/(?P<pk>[\w]+)/$', SedeDetailView.as_view(), name='sede'),
    url(r'^facultad/(?P<pk>[\w]+)$', FacultadInstanciaDetailView.as_view(), name='unidad'),
    url(r'^escuela/(?P<pk>[\w]+)/$', EscuelaInstanciaDetailView.as_view(), name='escuela'),
    url(r'^departamento/(?P<pk>[\w]+)/$', DepartamentoInstanciaDetailView.as_view(), name='departamento'),
    url(r'^carrera/(?P<pk>[\w]+)/$', CarreraInstanciaDetailView.as_view(), name='carrera'),

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
    url(r'^facultad/(?P<facultad_pk>[\w]+)/recursos/json/$', views.facultad_recursos_categoria, name='recursos-facultad'),
    url(r'^facultad/(?P<facultad_pk>[\w]+)/aulas/json/$', views.facultad_aulas_tipo, name='aulas-facultad'),
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


    # Reportes
    url(r'^prueba/reporte$', views.reporte_facultad_demo, name='reporte-prueba'),
    url(r'^facultad/(?P<facultad_pk>[\w]+)/reporte/$', views.reporte_facultad, name='reporte-facultad')
]
