from django.conf.urls import url
from solicitud import views

app_name = 'solicitud'
urlpatterns = [
    # Solicitud CRUD
    url(r'^$', views.UserSolicitudView.as_view(), name='propias'),
    url(r'^lista/$', views.SolicitudListview.as_view(), name='lista'),
    url(r'^(?P<pk>[\d]+)/$', views.SolicitudDetailView.as_view(), name='detalle'),
    url(r'^crear/$', views.SolicitudCreateView.as_view(), name='crear'),
    url(r'^(?P<pk>[\d]+)/editar/$', views.SolicitudUpdateView.as_view(), name='editar'),
    url(r'^(?P<pk>[\d]+)/resolver/$', views.ResolverSolicitudView.as_view(), name='resolver'),

    # Comentario CRUD
    url(r'^(?P<solicitud_pk>[\d]+)/comentario/$', views.crear_comentario, name='comentario'),

]
