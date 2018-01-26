from django import forms

from dal import autocomplete

from inventario.models import Fabricante, Categoria, Modelo, Equipo, Aula


class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ('nombre', 'url')
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del Fabricante',
            }),
            'url': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL Fabricante',
            })
        }
        labels = {
            'nombre': 'Nombre del Fabricante',
            'url': 'Direccion Web del Fabricante*'
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
            })
        }
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
        fields = ('etiqueta', 'aula', 'modelo', 'observaciones')
        widgets = {
            'modelo': autocomplete.ModelSelect2(
                url='inventario:modelo-autocomplete',
                attrs={
                    "class": "form-control",
                    "data-placeholder": "Modelo del Equipo"
                }),
            'etiqueta': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Etiqueta del Equipo'
            }),
            'aula': autocomplete.ModelSelect2(
                url='inventario:aula-autocomplete',
                attrs={
                "class": "form-control",
                "data-placeholder": "Aula en la que se encuentra el equipo",
            }),
        }
        labels = {
            'modelo': 'Modelo del Equipo',
            'etiqueta': 'Etiqueta del Equipo'
        }


class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ('numero', 'tipo')
        widgets = {
            'numero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Numero de Aula'
            }),
            'tipo': forms.Select(choices=Aula.TIPOS, attrs={
                'class': 'form-control'
            }),
        }


class BulkCreateForm(forms.Form):
    archivo = forms.FileField()
