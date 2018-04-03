from django import forms

from dal import autocomplete
from estudiantes.models import Estudiante, Anteproyecto, Proyecto


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
            'cod_sede', 'cod_facultad', 'cod_escuela', 'cod_carrera',
            'turno', 'fecha_ingreso', 'semestre_ingreso', 'ultimo_anio',
            'ultimo_semestre', 'fecha_graduacion'
        )
        widgets = {
        }


class AnteproyectoForm(forms.ModelForm):
    class Meta:
        model = Anteproyecto
        fields = ('estudiante', 'asesor', 'cod_carrera',
                  'nombre_proyecto', 'archivo', 'resumen')
        labels = {
            'cod_carrera': 'Codigo de la Carrera'
        }
        widgets = {
            'cod_carrera': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'nombre_proyecto': forms.TextInput(attrs={
                'placeholder': 'Nombre del Proyecto',
                'class': 'form-control'
            }),
            'resumen': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'archivo': forms.FileInput(attrs={
            }),
        }

    def __init__(self, *args, **kwargs):
        super(AnteproyectoForm, self).__init__(*args, **kwargs)


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = (
            'anteproyecto', 'jurados', 'fecha_entrega', 'fecha_sustentacion',
            'programa', 'nota', 'detalle', 'archivo'
        )
        widgets = {
            # 'anteproyecto': autocomplete.ModelSelect2(url='estudiante:anteproyecto-autocomplete', attrs={
            #     "class": "form-control",
            #     "data-placeholder": "Anteproyecto"
            # }),
            # 'jurados': autocomplete.ModelSelect2Multiple(url='perfil:autocomplete', attrs={
            #     "data-placeholder": "Jurados, Max. 3",
            #     "data-maximum-selection-length": 3,  # TODO: Limitar en backend
            # }),
            'programa': forms.Select(attrs={
                'class': 'form-control'
            }),
            'nota': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nota Obtenida'
            }),
            'fecha_sustentacion': forms.TextInput(attrs={
                'class': 'datepicker form-control',
                'placeholder': 'Fecha de Sustentacion'
            }),
            'fecha_entrega': forms.TextInput(attrs={
                'class': 'datepicker form-control',
                'placeholder': 'Fecha de Entrega'
            }),
            'detalle': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'archivo': forms.FileInput(attrs={

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
