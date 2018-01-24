from django.contrib import admin
from solicitud.models import Solicitud, Comentario

# Register your models here.
admin.site.register(Solicitud)
admin.site.register(Comentario)