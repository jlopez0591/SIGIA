# Django imports
from django.contrib import admin

# Third party
from import_export.admin import ImportExportMixin

#
from actividades.models import EstadiaPostdoctoral, Publicacion, Investigacion, Libro, Conferencia, Ponencia, \
    Proyecto, Premio, Actividad, InfoTitulo, Titulo, CentroEstudio, Idioma
from actividades.resources import PublicacionResources, EstadiaPostdoctoralResource, InvestigacionResource, \
    LibroResource, ConferenciaResource, PonenciaResource, ProyectoResource, PremioResource


class PublicacionAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = PublicacionResources


class EstadiaAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = EstadiaPostdoctoralResource


class InvestigacionAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = InvestigacionResource


class LibroAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = LibroResource


class ConferenciaAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ConferenciaResource


class PonenciaAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = PonenciaResource


class ProyectoAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ProyectoResource


class PremioAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = PremioResource


# Register your models here.
admin.site.register(EstadiaPostdoctoral, EstadiaAdmin)
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Investigacion, InvestigacionAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Conferencia, ConferenciaAdmin)
admin.site.register(Ponencia, PonenciaAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Premio, PremioAdmin)
admin.site.register(Actividad)
admin.site.register(InfoTitulo)
admin.site.register(Idioma)
admin.site.register(Titulo)
admin.site.register(CentroEstudio)