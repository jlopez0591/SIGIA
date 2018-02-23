from django.conf.urls import url
from core import views

app_name = 'core'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^password/reset/$', views.cambiar_password, name='cambiar-password'),
]
