from django.conf.urls import url
from actividades.views import ActivityCreateView, ActivityDetailView, ActivityUpdateView, ActividadesPendientes, \
    ActividadListView, ActividadesPropias, EstadiaCreateView
from actividades.forms import *
from actividades import views

app_name = 'actividad'
urlpatterns = [
    # General actividades
    url(r'^lista/$', ActividadListView.as_view(), name='lista'),
    url(r'^pendientes/$', views.actividades_pendientes, name='pendientes'),
    url(r'^propias/$', ActividadesPropias.as_view(), name='propias'),
    url(r'^(?P<pk>[0-9]+)/$', ActivityDetailView.as_view(), name='detalle'),
    url(r'^(?P<pk>[0-9]+)/aprobar/$', views.aprobar_actividad, name='aprobar'),

    # Estadia
    url(r'^estadia/crear/$', ActivityCreateView.as_view(model=EstadiaPostdoctoral, form_class=EstadiaForm,
                                                        template_name='actividades/estadia/crear.html'),
        name='crear-estadia'),
    url(r'^estadia/(?P<pk>[0-9]+)/editar/$',
        ActivityUpdateView.as_view(model=EstadiaPostdoctoral, form_class=EstadiaForm), name='actualizar-estadia'),

    # Publicacion
    url(r'^publicacion/crear/$', ActivityCreateView.as_view(model=Publicacion, form_class=PublicacionForm,
                                                            template_name='actividades/publicacion/crear.html'),
        name='crear-publicacion'),
    url(r'^publicacion/(?P<pk>[0-9]+)/editar/$',
        ActivityUpdateView.as_view(model=Publicacion, form_class=PublicacionForm), name='actualizar-publicacion'),

    # Investigacion
    url(r'^investigacion/crear/$', ActivityCreateView.as_view(model=Investigacion, form_class=InvestigacionForm,
                                                              template_name='actividades/investigacion_create_form.html'),
        name='crear-investigacion'),
    url(r'^investigacion/(?P<pk>[0-9]+)/editar/$',
        ActivityUpdateView.as_view(model=Investigacion, form_class=InvestigacionForm), name='actualizar-investigacion'),

    # Libro
    url(r'^libro/crear/$',
        ActivityCreateView.as_view(model=Libro, form_class=LibroForm, template_name='libro/crear.html'),
        name='crear-libro'),
    url(r'^libro/(?P<pk>[0-9]+)/editar/$', ActivityUpdateView.as_view(model=Libro, form_class=LibroForm),
        name='actualizar-libro'),

    # Conferencia
    url(r'^conferencia/crear/$', ActivityCreateView.as_view(model=Conferencia, form_class=ConferenciaForm,
                                                            template_name='conferencia/crear.html'),
        name='crear-conferencia'),
    url(r'^conferencia/(?P<pk>[0-9]+)/editar/$',
        ActivityUpdateView.as_view(model=Conferencia, form_class=ConferenciaForm), name='actualizar-conferencia'),

    # Ponencia
    url(r'^ponencia/crear/$',
        ActivityCreateView.as_view(model=Ponencia, form_class=PonenciaForm, template_name='ponencia/crear.html'),
        name='crear-ponencia'),
    url(r'^ponencia/(?P<pk>[0-9]+)/editar/$', ActivityUpdateView.as_view(model=Ponencia, form_class=PonenciaForm),
        name='actualizar-ponencia'),

    # Proyecto
    url(r'^proyecto/crear/$',
        ActivityCreateView.as_view(model=Proyecto, form_class=ProyectoForm, template_name='proyecto/crear.html'),
        name='crear-proyecto'),
    url(r'^proyecto/(?P<pk>[0-9]+)/editar/$', ActivityUpdateView.as_view(model=Proyecto, form_class=ProyectoForm),
        name='actualizar-proyecto'),

    # Premio
    url(r'^premio/crear/$',
        ActivityCreateView.as_view(model=Premio, form_class=PremioForm, template_name='premio/crear.html'),
        name='crear-premio'),
    url(r'^premio/(?P<pk>[0-9]+)/editar/$', ActivityUpdateView.as_view(model=Premio, form_class=PremioForm),
        name='actualizar-premio'),

    # Idiomas
    url(r'^idioma/crear/$',
        ActivityCreateView.as_view(model=Idioma, form_class=IdiomaForm, template_name='idioma/crear.html'),
        name='crear-idioma'),
    url(r'^idioma/(?P<pk>[0-9]+)/editar/$', ActivityUpdateView.as_view(model=Idioma, form_class=IdiomaForm),
        name='editar-idioma'),

    # Titulo
    url(r'^titulo/crear/$',
        ActivityCreateView.as_view(model=Titulo, form_class=TituloForm, template_name='titulo/crear.html'),
        name='crear-titulo'),
    url(r'^titulo/(?P<pk>[0-9]+)/editar/$', ActivityCreateView.as_view(model=Titulo, form_class=TituloForm),
        name='crear-titulo')
]
