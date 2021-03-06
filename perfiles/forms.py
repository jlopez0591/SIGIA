from django import forms
from perfiles.models import Perfil


class PerfilAdminForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = (
            'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido',
            'fecha_nacimiento', 'sexo',
            'provincia', 'clase', 'tomo', 'folio',
            'imagen', 'pais',
            'categoria',
            'cod_sede', 'cod_facultad', 'cod_departamento',
            'cod_escuela', 'cod_profesor', 'fecha_inicio')
        labels = {
            'primer_nombre': 'Primer Nombre',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'categoria': 'Dedicacion',
            'cod_sede': 'Codigo de Sede',
            'cod_facultad': 'Codigo de Facultad',
            'cod_departamento': 'Codigo de Departamento',
            'cod_escuela': 'Codigo de Escuela',
            'cod_profesor': 'Codigo de Profesor'
        }
        widgets = {
            'primer_nombre': forms.TextInput(attrs={
                'class': 'form-control',
                # 'disabled': True,
                'placeholder': "Primer Nombre",
            }),
            'segundo_nombre': forms.TextInput(attrs={
                'class': 'form-control',
                # 'disabled': True,
                'placeholder': "Segundo Nombre",
            }),
            'primer_apellido': forms.TextInput(attrs={
                'class': 'form-control',
                # 'disabled': True,
                'placeholder': "Apellido Paterno",
            }),
            'segundo_apellido': forms.TextInput(attrs={
                'class': 'form-control',
                # 'disabled': True,
                'placeholder': "Apellido Materno o de Casada",
            }),
            'provincia': forms.Select(attrs={
                'class': 'form-control',
                ## 'disabled': True,
                'placeholder': "Provincia",
            }),
            'clase': forms.Select(attrs={
                'class': 'form-control cedula',
                ## 'disabled': True,
                'placeholder': "Clase",
            }),
            'tomo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tomo'
            }),
            'folio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Folio'
            }),
            'fecha_nacimiento': forms.TextInput(attrs={
                'class': 'datepicker form-control',
                'placeholder': 'YYYY-MM-DD'
            }),
            'fecha_inicio': forms.TextInput(attrs={
                'class': 'datepicker form-control',
                'label': 'Fecha de Incio de Labores',
                'placeholder': 'YYYY-MM-DD',
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
                # 'disabled': True,
                'placeholder': "Apellido Materno",
            }),
            'cod_facultad': forms.TextInput(attrs={
                'class': 'form-control',
                # 'disabled': True,
                'placeholder': "Apellido Materno",
            }),
            'cod_departamento': forms.TextInput(attrs={
                'class': 'form-control',
                # 'disabled': True,
                'placeholder': "Apellido Materno",
            }),
            'cod_escuela': forms.TextInput(attrs={
                'class': 'form-control',
                # 'disabled': True,
                'placeholder': "Apellido Materno",
            }),
            "cod_profesor": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Codigo de Profesor',
                'label': 'Codigo de Profesor'
            })
        }


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = (
            'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido',
            'fecha_nacimiento', 'sexo',
            'provincia', 'clase', 'tomo', 'folio',
            'imagen', 'pais',
            'categoria',
            'cod_sede', 'cod_facultad', 'cod_departamento',
            'cod_escuela', 'cod_profesor', 'fecha_inicio')
        labels = {
            'primer_nombre': 'Primer Nombre',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'categoria': 'Dedicacion',
            'cod_sede': 'Codigo de Sede',
            'cod_facultad': 'Codigo de Facultad',
            'cod_departamento': 'Codigo de Departamento',
            'cod_escuela': 'Codigo de Escuela',
            'cod_profesor': 'Codigo de Profesor'
        }
        widgets = {
            'primer_nombre': forms.TextInput(attrs={
                'class': 'form-control',
                # 'disabled': True,
                'placeholder': "Primer Nombre",
            }),
            'segundo_nombre': forms.TextInput(attrs={
                'class': 'form-control',
                # 'disabled': True,
                'placeholder': "Segundo Nombre",
            }),
            'primer_apellido': forms.TextInput(attrs={
                'class': 'form-control',
                # 'disabled': True,
                'placeholder': "Apellido Paterno",
            }),
            'segundo_apellido': forms.TextInput(attrs={
                'class': 'form-control',
                # 'disabled': True,
                'placeholder': "Apellido Materno o de Casada",
            }),
            'provincia': forms.Select(attrs={
                'class': 'form-control',
                ## 'disabled': True,
                'placeholder': "Provincia",
            }),
            'clase': forms.Select(attrs={
                'class': 'form-control cedula',
                ## 'disabled': True,
                'placeholder': "Clase",
            }),
            'tomo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tomo'
            }),
            'folio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Folio'
            }),
            'fecha_nacimiento': forms.TextInput(attrs={
                'class': 'datepicker form-control',
                'placeholder': 'YYYY-MM-DD'
            }),
            'fecha_inicio': forms.TextInput(attrs={
                'class': 'datepicker form-control',
                'label': 'Fecha de Incio de Labores',
                'placeholder': 'YYYY-MM-DD',
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
                # 'disabled': True,
                'placeholder': "Apellido Materno",
            }),
            'cod_facultad': forms.TextInput(attrs={
                'class': 'form-control',
                # 'disabled': True,
                'placeholder': "Apellido Materno",
            }),
            'cod_departamento': forms.TextInput(attrs={
                'class': 'form-control',
                # 'disabled': True,
                'placeholder': "Apellido Materno",
            }),
            'cod_escuela': forms.TextInput(attrs={
                'class': 'form-control',
                # 'disabled': True,
                'placeholder': "Apellido Materno",
            }),
            "cod_profesor": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Codigo de Profesor',
                'label': 'Codigo de Profesor'
            })
        }
