from django.conf.urls import url
from core import views

app_name = 'core'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^password/reset/$', views.cambiar_password, name='cambiar-password'),
    url(r'^demo/info', views.info_demo, name='demo'),
    url(r'^info/$', views.info_sitio, name='info')
    # Reportes
    # TODO: Reporte Facultad
    # TODO: Reporte Escuela
    # TODO: Reporte Departamento
    # TODO: Reporte Carrera
    # TODO: Reporte Personal
]
