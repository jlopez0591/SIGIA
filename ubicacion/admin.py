from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from ubicacion.models import *


class SedeResource(resources.ModelResource):
    class Meta:
        model = Sede


class FacultadResource(resources.ModelResource):
    class Meta:
        model = Facultad


class EscuelaResource(resources.ModelResource):
    class Meta:
        model = Escuela


class DepartamentoResource(resources.ModelResource):
    class Meta:
        model = Departamento


class CarreraResource(resources.ModelResource):
    class Meta:
        model = Carrera


class FacultadInstanciaResource(resources.ModelResource):
    class Meta:
        model = FacultadInstancia


class EscuelaInstanciaResource(resources.ModelResource):
    class Meta:
        model = EscuelaInstancia


class DepartamentoInstanciaResource(resources.ModelResource):
    class Meta:
        model = DepartamentoInstancia


class CarreraInstanciaResource(resources.ModelResource):
    class Meta:
        model = CarreraInstancia


class SedeModelAdmin(ImportExportModelAdmin):
    resource_class = SedeResource


class FacultadModelAdmin(ImportExportModelAdmin):
    resource_class = FacultadResource


class EscuelaModelAdmin(ImportExportModelAdmin):
    resource_class = EscuelaResource


class DepartamentoModelAdmin(ImportExportModelAdmin):
    resource_class = DepartamentoResource


class CarreraModelAdmin(ImportExportModelAdmin):
    resource_class = CarreraResource


class FacultadInstanciaModelAdmin(ImportExportModelAdmin):
    resource_class = FacultadInstanciaResource


class EscuelaInstanciaModelAdmin(ImportExportModelAdmin):
    resource_class = EscuelaInstanciaResource


class CarreraInstanciaModelAdmin(ImportExportModelAdmin):
    resource_class = CarreraInstanciaResource


# Register your models here.
admin.site.register(Sede, SedeModelAdmin)
admin.site.register(Facultad, FacultadInstanciaModelAdmin)
admin.site.register(Escuela, EscuelaModelAdmin)
admin.site.register(Departamento, DepartamentoModelAdmin)
admin.site.register(Carrera, CarreraModelAdmin)
admin.site.register(FacultadInstancia, FacultadInstanciaModelAdmin)
admin.site.register(EscuelaInstancia, EscuelaInstanciaModelAdmin)
admin.site.register(DepartamentoInstancia, DepartamentoModelAdmin)
admin.site.register(CarreraInstancia, CarreraInstanciaModelAdmin)
