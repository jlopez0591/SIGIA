from django.forms import ModelForm, TextInput
from django import forms

from actividades.models import Actividad, EstadiaPostdoctoral, Publicacion, Investigacion, Libro, Conferencia, Ponencia, \
    Premio, Titulo, Idioma, Proyecto


class RechazarForm(ModelForm):
    class Meta:
        model = Actividad
        fields = ('motivo_rechazo',)


class EstadiaForm(ModelForm):
    class Meta:
        model = EstadiaPostdoctoral
        fields = ('nombre_actividad', 'lugar', 'fecha', 'resumen', 'archivo',)
        widgets = {
            "nombre_actividad": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Nombre de la Actividad"
            }),
            "lugar": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Lugar donde se realizo la Estadia"
            }),  # TextInput(attrs={})
            "fecha": TextInput(attrs={
                'class': 'datepicker form-control',
                "placeholder": "Fecha en que se realizo la Estadia (YYYY-MM-DD)"
            }),
            "resumen": forms.Textarea(attrs={
                'class': 'form-control',
            }),
            "archivo": "",
        }

    def full_clean(self):
        super(EstadiaForm, self).full_clean()
        try:
            self.instance.validate_unique()
        except forms.ValidationError as e:
            self._update_errors(e)


class PublicacionForm(ModelForm):
    class Meta:
        model = Publicacion
        fields = ('nombre_actividad', 'lugar_publicacion', 'fecha', 'resumen', 'archivo')
        widgets = {
            "nombre_actividad": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Nombre de la publicacion"
            }),
            "lugar_publicacion": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Lugar donde se realizo la publicacion"
            }),
            "fecha": TextInput(attrs={
                'class': 'datepicker form-control',
                "placeholder": "Fecha de Publicacion (YYYY-MM-DD)"
            }),
            "resumen": forms.Textarea(attrs={
            }),
            "archivo": "",
        }


class InvestigacionForm(ModelForm):
    class Meta:
        model = Investigacion
        fields = ('nombre_actividad', 'codigo', 'fecha', 'resumen', 'archivo',)
        widgets = {
            "nombre_actividad": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Nombre de la Actividad"
            }),
            "codigo": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Codigo de la Actividad"
            }),
            "fecha": TextInput(attrs={
                "class": "datepicker form-control",
                "placeholder": "Fecha en que se inicio la Investigacion (YYYY-MM-DD)"
            }),
            "resumen": forms.Textarea(attrs={
            }),
            "archivo": ""
        }


class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = ("nombre_actividad", "editorial", "isbn", "fecha", "resumen", "archivo",)
        widgets = {
            "nombre_actividad": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Nombre del Libro",
            }),
            "editorial": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Nombre de la Editorial"
            }),
            "isbn": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Codigo ISBN"
            }),
            "fecha": TextInput(attrs={
                'class': 'datepicker form-control',
                "placeholder": "Fecha de Publicacion (YYYY-MM-DD)"
            }),
            "resumen": forms.Textarea(attrs={
            }),
            "archivo": ""
        }


class ConferenciaForm(ModelForm):
    class Meta:
        model = Conferencia
        fields = ('nombre_actividad', 'fecha', 'resumen', 'archivo')
        widgets = {
            "nombre_actividad": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Nombre de la Conferencia",
            }),
            "fecha": TextInput(attrs={
                'class': 'datepicker form-control',
                "placeholder": "Fecha en que se realizo la conferencia (YYYY-MM-DD)"
            }),
            "resumen": forms.Textarea(attrs={
            }),
            "archivo": ""
        }


class PonenciaForm(ModelForm):
    class Meta:
        model = Ponencia
        fields = ('nombre_actividad', 'pais', 'fecha', 'resumen', 'archivo',)
        widgets = {
            "nombre_actividad": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Nombre de la Actividad"
            }),
            "pais": forms.Select(attrs={
                'class': 'form-control',
                "placeholder": "Pais donde se realizo la ponencia"
            }),
            "fecha": TextInput(attrs={
                "placeholder": "Fecha en que se realizo la ponencia (YYYY-MM-DD)",
                'class': 'datepicker form-control',
            }),
            "resumen": forms.Textarea(),
            "archivo": ""
        }


class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre_actividad', 'tipo', 'fecha', 'resumen', 'archivo',)
        widgets = {
            "nombre_actividad": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Nombre del proyecto"
            }),
            "tipo": forms.Select(attrs={
                'class': 'form-control',
                "placeholder": "Tipo del proyecto"
            }),
            "fecha": TextInput(attrs={
                'class': 'datepicker form-control',
                "placeholder": "Fecha en que se realizo el proyecto (YYYY-MM-DD)",
            }),
        }


class PremioForm(ModelForm):
    class Meta:
        model = Premio
        fields = ('nombre_actividad', 'tipo', 'fecha', 'resumen', 'archivo',)
        widgets = {
            "nombre_actividad": TextInput(attrs={
                "placeholder": "Nombre del premio",
                'class': 'form-control',
            }),
            "fecha": TextInput(attrs={
                'class': 'datepicker',
                "placeholder": "Fecha en que se recibio el premio (YYYY-MM-DD)",
            }),
        }


class TituloForm(ModelForm):
    class Meta:
        model = Titulo
        fields = ('info_titulo', 'centro_estudio', 'fecha', 'resumen', 'archivo',)
        widgets = {
            "info_titulo": forms.Select(attrs={
                "placeholder": "Titulo Adquirido",
                'class': 'form-control',
            }),
            "centro_estudio": forms.Select(attrs={
                "placeholder": "Centro de Estudio donde Adquirio el titulo"
            }),
            "fecha": TextInput(attrs={
                'class': 'datepicker',
                "placeholder": "Fecha en que obtuvo el titulo (YYYY-MM-DD)",
            }),
        }


class IdiomaForm(ModelForm):
    class Meta:
        model = Idioma
        fields = ('nombre', 'nivel_hablado', 'nivel_escrito',)
