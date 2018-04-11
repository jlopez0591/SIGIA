"""sigia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
                  # Mis apps
                  url(r'^', include('core.urls')),
                  url(r'^actividad/', include('actividades.urls')),
                  url(r'^estudiante/', include('estudiantes.urls')),
                  url(r'^inventario/', include('inventario.urls')),
                  # url(r'^perfil/', include('perfiles.urls')),
                  url(r'^solicitud/', include('solicitud.urls')),
                  url(r'^', include('ubicacion.urls')),
                  # Django apps
                  url(r'^login/$', auth_views.login, name='login'),
                  url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
                  url(r'^admin/', admin.site.urls),
              ]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

