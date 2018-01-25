from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from dal import autocomplete

from inventario.models import Fabricante, Categoria, Modelo, Equipo


class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ('nombre', 'url')
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del Fabricante', }),
            'url': forms.TextInput(attrs={'placeholder': 'Direccion Web del Fabricante', })
        }
        labels = {
            'nombre': 'Nombre del Fabricante',
            'url': 'Direccion Web del Fabricante*'
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)
        labels = {
            'nombre': 'Nombre de la Categoria'
        }


class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ('nombre', 'fabricante', 'categoria', 'url')
        widgets = {
            'fabricante': autocomplete.ModelSelect2(url='inventario:fabricante-autocomplete'),
            'categoria': autocomplete.ModelSelect2(url='inventario:categoria-autocomplete')
        }
        labels = {
            'fabricante': 'Nombre del Fabricante',
            'categoria': 'Categoria',
            'nombre': 'Nombre del Modelo'
        }


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ('etiqueta', 'modelo', 'observaciones')
        widgets = {
            'modelo': autocomplete.ModelSelect2(url='inventario:modelo-autocomplete',
                                                attrs={"data-placeholder": "Modelo del Equipo"}),
            'etiqueta': forms.TextInput(attrs={
                'placeholder': 'Etiqueta del Equipo'
            })
        }
        labels = {
            'modelo': 'Modelo del Equipo',
            'etiqueta': 'Etiqueta del Equipo'
        }


class BulkCreateForm(forms.Form):
    archivo = forms.FileField()
