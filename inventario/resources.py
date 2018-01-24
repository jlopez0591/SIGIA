from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from inventario.models import Categoria, Fabricante, Modelo


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria


class FabricanteResource(resources.ModelResource):
    class Meta:
        model = Fabricante


class ModeloResource(resources.ModelResource):
    categoria = fields.Field(
        column_name='categoria',
        attribute='categoria',
        widget=ForeignKeyWidget(Categoria, 'nombre')
    )
    fabricante = fields.Field(
        column_name='fabricante',
        attribute='fabricante',
        widget=ForeignKeyWidget(Fabricante, 'nombre')
    )

    class Meta:
        model = Modelo


class EquipoResource(resources.ModelResource):
    pass
