from django import forms
from dal import autocomplete
from django.core.exceptions import ValidationError
from estudiantes.models import Estudiante, TrabajoGraduacion
from core.models import Usuario


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
        labels = {
            'provincia': '',
            'clase': '',
            'tomo': '',
            'folio': ''
        }
        widgets = {
            'primer_nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'segundo_nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'primer_apellido': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'segundo_apellido': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'provincia': forms.Select(attrs={
                'class': 'form-control cedula',
                'disabled': 'true'
            }),
            'clase': forms.Select(attrs={
                'class': 'form-control cedula'
            }),
            'tomo': forms.TextInput(attrs={
                'class': 'form-control cedula'
            }),
            'folio': forms.TextInput(attrs={
                'class': 'form-control cedula'
            }),
            'sexo': forms.Select(attrs={
                'class': 'form-control'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'fecha_nacimiento': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'discapacidad': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'tipo_sangre': forms.Select(attrs={
                'class': 'form-control'
            }),
            'pais': forms.Select(attrs={
                'class': 'form-control'
            }),
            'correo': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'telefono_oficina': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'celular': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'celular_oficina': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'cod_sede': forms.TextInput(attrs={
                'class': 'form-control carrera'
            }),
            'cod_facultad': forms.TextInput(attrs={
                'class': 'form-control carrera'
            }),
            'cod_escuela': forms.TextInput(attrs={
                'class': 'form-control carrera'
            }),
            'cod_carrera': forms.TextInput(attrs={
                'class': 'form-control carrera'
            }),
            'turno': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'fecha_ingreso': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'semestre_ingreso': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'ultimo_anio': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'ultimo_semestre': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'fecha_graduacion': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }


class TrabajoForm(forms.ModelForm):
    class Meta:
        model = TrabajoGraduacion
        fields = ('nombre_proyecto', 'estudiantes', 'asesor', 'estado', 'programa',
                  'cod_carrera', 'fecha_entrega', 'fecha_sustentacion', 'jurados', 'nota',
                  'archivo_anteproyecto', 'archivo_trabajo')
        labels = {
            'cod_carrera': 'Codigo de Carrera',
            'nombre_proyecto': 'Nombre del Proyecto',
            'fecha_entrega': 'Fecha de Entrega',
            'fecha_sustentacion': 'Fecha de Sustentacion',
            'nota': 'Nota Obtenida',
        }
        widgets = {
            'cod_carrera': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'nombre_proyecto': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'estudiantes': forms.SelectMultiple(),
            'asesor': forms.Select(attrs={
                'class': 'custom-select form-control'
            }),
            'estado': forms.Select(attrs={
                'class': 'custom-select form-control'
            }),
            'programa': forms.Select(attrs={
                'class': 'custom-select form-control'
            }),
            'fecha_entrega': forms.TextInput(attrs={
                'class': 'form-control datepicker'
            }),
            'fecha_sustentacion': forms.TextInput(attrs={
                'class': 'form-control datepicker'
            }),
            'nota': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'archivo_anteproyecto': forms.FileInput(attrs={
                'class': 'form-control-file'
            }),
            'archivo_trabajo': forms.FileInput(attrs={
                'class': 'form-control-file'
            })
        }
        placeholder = {
            'fecha_sustentacion': 'yyyy-mm-dd'
        }

    def __init__(self, *args, **kwargs):
        facultad = kwargs.pop('facultad')
        super(TrabajoForm, self).__init__(*args, **kwargs)
        self.fields['estudiantes'].queryset = Estudiante.objects.activos().filter(facultad=facultad)


    def clean(self):
        estudiantes = self.cleaned_data.get('estudiantes')
        jurados = self.cleaned_data.get('jurados')
        if estudiantes.count() > 3:
            raise ValidationError('Seleccione 3 estudiantes max.')
        if jurados.count() > 3:
            raise ValidationError('Seleccione 3 jurados max.')
        return self.cleaned_data
