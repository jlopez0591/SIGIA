from django import forms
from perfiles.models import Perfil


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = (
            'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'fecha_nacimiento',
            'fecha_inicio',
            'sexo', 'provincia', 'clase', 'tomo', 'folio',
            'imagen', 'categoria', 'pais', 'cod_sede', 'cod_unidad', 'cod_seccion')
        widgets = {
            'primer_nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True,
                'placeholder': "Primer Nombre",
            }),
            'segundo_nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True,
                'placeholder': "Segundo Nombre",
            }),
            'primer_apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True,
                'placeholder': "Apellido Paterno",
            }),
            'segundo_apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True,
                'placeholder': "Apellido Materno",
            }),
            'provincia': forms.Select(attrs={
                'class': 'form-control',
                #'disabled': True,
                'placeholder': "Apellido Materno",
            }),
            'clase': forms.Select(attrs={
                'class': 'form-control cedula',
                #'disabled': True,
                'placeholder': "Apellido Materno",
            }),
            'tomo': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'folio': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'fecha_nacimiento': forms.TextInput(attrs={
                'class': 'datepicker form-control',
                'placeholder': 'Fecha de Inicio de Labores'
            }),
            'fecha_inicio': forms.TextInput(attrs={
                'class': 'datepicker form-control',
                'placeholder': 'Fecha de Inicio de Labores',
            }),
            'sexo': forms.Select(attrs={
                'class': 'form-control'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
            'pais': forms.Select(attrs={
                'class': 'form-control'
            }),
            'cod_sede': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True,
                'placeholder': "Apellido Materno",
            }),
            'cod_unidad': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True,
                'placeholder': "Apellido Materno",
            }),
            'cod_seccion': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True,
                'placeholder': "Apellido Materno",
            }),
        }

class PerfilTestForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('__all__')
