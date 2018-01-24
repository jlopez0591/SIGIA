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
            'provincia': forms.TextInput(attrs={
                'class': 'form-control cedula-field',
                'disabled': True,
                'placeholder': "Apellido Materno",
            }),
            'clase': forms.TextInput(attrs={
                'class': 'form-control cedula-field',
                'disabled': True,
                'placeholder': "Apellido Materno",
            }),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'datepicker'}),
            'fecha_inicio': forms.TextInput(attrs={'class': 'datepicker'}),
        }
