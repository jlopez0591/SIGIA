from django.contrib import admin

from estudiantes.forms import AnteproyectoForm
from estudiantes.models import Estudiante, Anteproyecto, TrabajoGraduacion

from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class AnteproyectoAdmin(admin.ModelAdmin):
    form = AnteproyectoForm


class EstudianteResource(resources.ModelResource):
    class Meta:
        model = Estudiante


class EstudianteImportExportModelAdmin(ImportExportModelAdmin):
    resource_class = EstudianteResource


admin.site.register(Estudiante, EstudianteImportExportModelAdmin)
admin.site.register(Anteproyecto)
admin.site.register(TrabajoGraduacion)
