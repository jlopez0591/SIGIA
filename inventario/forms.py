from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from dal import autocomplete

from inventario.models import Fabricante, Categoria, Modelo, Equipo


class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ('nombre',)
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del Fabricante', })
        }


class CategoriaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = 'Nombre de la categoria'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Categoria',
                'nombre',
            ),
            ButtonHolder(
                Submit('Registrar', 'Registrar', css_class='btn btn-block btn-primary btn-lg')
            )
        )

    class Meta:
        model = Categoria
        fields = ('nombre',)


class ModeloForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModeloForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = 'Nombre del Modelo'
        self.fields['fabricante'].label = 'Nombre del Fabricante'
        self.fields['categoria'].label = 'Categoria del Modelo'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Modelo',
                'nombre',
                'fabricante',
                'categoria'
            ),
            ButtonHolder(
                Submit('Registrar', 'Registrar', css_class='btn btn-block btn-primary btn-lg')
            )
        )

    class Meta:
        model = Modelo
        fields = ('nombre', 'fabricante', 'categoria',)
        widgets = {
            'fabricante': autocomplete.ModelSelect2(url='inventario:fabricante-autocomplete'),
            'categoria': autocomplete.ModelSelect2(url='inventario:categoria-autocomplete')
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


class BulkCreateForm(forms.Form):
    archivo = forms.FileField()
