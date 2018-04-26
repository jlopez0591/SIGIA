from django.conf.urls import url
from estudiantes.views import *


app_name = 'estudiante'
urlpatterns = [
    url(r'^(?P<pk>[\d]+)/$', EstudianteDetailView.as_view(), name='detalle'),
    url(r'^(?P<pk>[\d]+)/editar/$', EstudianteUpdateView.as_view(), name='editar'),
    url(r'^consulta/$', EstudianteListView.as_view(), name='lista'),
    url(r'^trabajo/crear/$', TrabajoGraduacionCreateView.as_view(), name='crear-trabajo'),
    url(r'^trabajo/(?P<pk>[\d]+)/$', TrabajoGraduacionDetailView.as_view(), name='detalle-trabajo'),
    url(r'^trabajo/(?P<pk>[\d]+)/editar/$', TrabajoGraduacionUpdateView.as_view(), name='editar-trabajo'),
    url(r'^facultad/(?P<pk>[\d]+)/trabajos/$', TrabajoGraduacionFacultadListView.as_view(), name='trabajo-facultad'),
    url(r'^escuela/(?P<pk>[\d]+)/trabajos/$', TrabajoGraduacionEscuelaListView.as_view(), name='trabajo-escuela'),
    url(r'^facultad/(?P<pk>[\d]+)/estudiantes/$', EstudianteFacultadListview.as_view(), name='estudiante-facultad'),
    url(r'^escuela/(?P<pk>[\d]+)/estudiantes/$', EstudianteEscuelaListView.as_view(), name='estudiante-escuela'),
    url(r'^escuela/(?P<pk>[\d]+)/trabajos/pendientes/$', TrabajoGraduacionPendienteListView.as_view(),
        name='trabajo-pendiente'),

    # Para el admin
    url(r'^trabajos/$', TrabajoGraduacionListView.as_view(), name='trabajos'),
    url(r'^estudiantes/$', EstudianteListView.as_view(), name='lista'),
]
