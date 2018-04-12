from django.contrib import admin
from estudiantes.models import Estudiante, TrabajoGraduacion

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class EstudianteResource(resources.ModelResource):
    class Meta:
        model = Estudiante


class EstudianteImportExportModelAdmin(ImportExportModelAdmin):
    resource_class = EstudianteResource


admin.site.register(Estudiante, EstudianteImportExportModelAdmin)
admin.site.register(TrabajoGraduacion)

