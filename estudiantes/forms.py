from django import forms
from django.forms import ModelForm, TextInput

from dal import autocomplete
from estudiantes.models import Estudiante, Anteproyecto, Proyecto

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = (
            # Info del nombre
            'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido',
            # Info de la cedula
            'provincia', 'clase', 'tomo', 'folio',
            # Info Personal
            'sexo', 'direccion', 'telefono', 'fecha_nacimiento',
            'discapacidad', 'tipo_sangre',
            # Info de contacto
            'pais', 'correo', 'telefono_oficina', 'celular',
            'celular_oficina',
            # Info academica
            'cod_sede', 'cod_unidad', 'cod_seccion', 'cod_carrera',
            'turno', 'fecha_ingreso', 'semestre_ingreso', 'ultimo_anio',
            'ultimo_semestre', 'fecha_graduacion'
        )
        widgets = {
        }


class AnteproyectoForm(forms.ModelForm):
    class Meta:
        model = Anteproyecto
        fields = ('estudiante', 'asesor', 'carrera',
                  'nombre_proyecto', 'archivo', 'resumen')
        widgets = {
            'estudiante': autocomplete.ModelSelect2Multiple(url='estudiante:autocomplete', attrs={
                "data-placeholder": "Estudiantes, Max. 3",
                "data-maximum-selection-length": 3,  # TODO: Limitar en el backend
            }),
            'asesor': autocomplete.ModelSelect2(url='perfil:autocomplete', attrs={
                "data-placeholder": "Profesor Asesor"
            }),
            'nombre_proyecto': TextInput(attrs={
                'placeholder': 'Nombre del Proyecto',
                'class': 'form-control'
            }),
            'carrera': autocomplete.ModelSelect2(url='ubicacion:carrera-autocomplete', attrs={
                "data-placeholder": "Carrera"
            }),
            'resumen': forms.TextInput(attrs={
                'label': 'Prueba'
            }),
            'archivo': '',
        }


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = (
            'anteproyecto', 'jurados', 'fecha_entrega', 'fecha_sustentacion',
            'programa', 'nota', 'detalle', 'archivo'
        )
        widgets = {
            'anteproyecto': autocomplete.ModelSelect2(url='estudiante:anteproyecto-autocomplete', attrs={
                "data-placeholder": "Anteproyecto"
            }),
            'jurados': autocomplete.ModelSelect2Multiple(url='perfil:autocomplete', attrs={
                "data-placeholder": "Jurados, Max. 3",
                "data-maximum-selection-length": 3,  # TODO: Limitar en backend
            }),
            'programa': '',
            'nota': forms.TextInput(attrs={
                'placeholder': 'Nota Obtenida'
            }),
            'fecha_sustentacion': forms.TextInput(attrs={
                'class': 'datepicker',
                'placeholder': 'Fecha de Sustentacion'
            }),
            'fecha_entrega': forms.TextInput(attrs={
                'class': 'datepicker',
                'placeholder': 'Fecha de Entrega'
            })
        }


class EstudianteFilterForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('provincia', 'clase', 'tomo', 'folio')
        widgets = {
            'provincia': forms.TextInput(attrs={'class': 'form-control'}),
            'clase': forms.TextInput(attrs={'class': 'form-control'}),
            'tomo': forms.TextInput(attrs={'class': 'form-control'}),
            'folio': forms.TextInput(attrs={'class': 'form-control'}),
        }
