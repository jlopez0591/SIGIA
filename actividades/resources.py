from import_export import resources
from .models import EstadiaPostdoctoral, Publicacion, Investigacion, Libro, Conferencia, Ponencia, Proyecto, Premio


class EstadiaPostdoctoralResource(resources.ModelResource):
    class Meta:
        model = EstadiaPostdoctoral


class PublicacionResources(resources.ModelResource):
    class Meta:
        model = Publicacion


class InvestigacionResource(resources.ModelResource):
    class Meta:
        model = Investigacion


class LibroResource(resources.ModelResource):
    class Meta:
        model = Libro


class ConferenciaResource(resources.ModelResource):
    class Meta:
        model = Conferencia


class PonenciaResource(resources.ModelResource):
    class Meta:
        model = Ponencia


class ProyectoResource(resources.ModelResource):
    class Meta:
        model = Proyecto


class PremioResource(resources.ModelResource):
    class Meta:
        model = Premio
