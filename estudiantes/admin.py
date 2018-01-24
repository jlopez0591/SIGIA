from django.contrib import admin

from estudiantes.forms import AnteproyectoForm
from estudiantes.models import Estudiante, Anteproyecto, Proyecto
# Register your models here.
class AnteproyectoAdmin(admin.ModelAdmin):
    form = AnteproyectoForm

admin.site.register(Estudiante)
admin.site.register(Anteproyecto)
admin.site.register(Proyecto)