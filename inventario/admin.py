from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from inventario.models import Fabricante, Categoria, Modelo, Equipo


# Register your models here.

@admin.register(Fabricante)
class FabricanteAdmin(ImportExportModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(ImportExportModelAdmin):
    pass

@admin.register(Modelo)
class ModeloAdmin(ImportExportModelAdmin):
    pass

@admin.register(Equipo)
class EquipoAdmin(ImportExportModelAdmin):
    pass

