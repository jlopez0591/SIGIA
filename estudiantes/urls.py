from django.conf.urls import url
from estudiantes.views import *
from estudiantes import views

app_name = 'estudiante'
urlpatterns = [
    # Students
    url(r'^(?P<pk>[\d]+)/$', EstudianteDetailView.as_view(), name='detalle'),
    url(r'^(?P<pk>[\d]+)/editar/$', EstudianteUpdateView.as_view(), name='editar'),
    url(r'^consulta/$', EstudianteListView.as_view(), name='lista'),

    url(r'^anteproyecto/crear/$', AnteproyectoCreateView.as_view(), name='crear-anteproyecto'),
    url(r'^anteproyecto/(?P<pk>[\d]+)/editar/$', AnteproyectoUpdateView.as_view(), name='editar-anteproyecto'),
    url(r'^anteproyecto/(?P<pk>[\d]+)/detalle/$', AnteproyectoDetailView.as_view(), name='anteproyecto-detalle'),
    url(r'^anteproyecto/(?P<pk>[\d]+)/aprobar/$', aprobar_anteproyecto, name='aprobar-anteproyecto'),
    url(r'^anteproyecto/(?P<pk>[\d]+)/rechazar/$', rechazar_anteproyecto, name='rechazar-anteproyecto'),
    url(r'^anteproyectos/pendientes/$', anteproyectos_pendientes, name='lista-anteproyectos'),
    url(r'^anteproyectos/$', views.anteproyectos_facultad, name='anteproyectos-unidad'),

    # Proyects
    url(r'^proyectos/$', views.proyectos_facultad, name='proyectos-facultad'),
    url(r'^proyecto/crear/$', ProyectoCreateView.as_view(), name='crear-proyecto'),
    url(r'^proyecto/(?P<pk>[\d]+)/editar/$', ProyectoUpdateView.as_view(), name='editar-proyecto'),
    url(r'^proyecto/(?P<pk>[\d]+)/detalle/$', ProyectoDetailView.as_view(), name='detalle-proyecto'),

    # Autocomplete views
    url(r'^autocomplete/$', EstudianteAutocomplete.as_view(), name='autocomplete'),
    url(r'^autocomplete/anteproyectos$', AnteproyectoAutocomplete.as_view(), name='anteproyecto-autocomplete'),

    # Report views
    url(r'^(?P<pk>[\d]+)/reporte$', views.reporte_estudiante, name='reporte'),

    # APIv2
    url(r'^facultad/(?P<pk>[\d]+)/$', EstudianteFacultadListview.as_view(), name='estudiante-facultad'),
    url(r'^escuela/(?P<pk>[\d]+)/$', EstudianteEscuelaListView.as_view(), name='estudiante-escuela'),

    url(r'^facultad/(?P<pk>[\d]+)/anteproyectos/$', AnteproyectoFacultadListView.as_view(),
        name='anteproyecto-facultad'),
    url(r'^escuela/(?P<pk>[\d]+)/anteproyectos/$', AnteproyectoEscuelaListView.as_view(), name='anteproyecto-escuela'),
    url(r'^escuela/(?P<pk>[\d]+)/anteproyectos/pendientes$', AnteproyectoPendienteEscuelaListView.as_view(),
        name='anteproyecto-escuela-pendiente'),

    url(r'^facultad/(?P<pk>[\d]+)/proyectos/$', EstudianteFacultadListview.as_view(), name='proyecto-facultad'),
    url(r'^escuela/(?P<pk>[\d]+)/proyectos/$', EstudianteEscuelaListView.as_view(), name='proyecto-escuela'),

]
