# Django imports
from django import forms
from django.conf.global_settings import LANGUAGES

from django.forms import ModelForm, TextInput
from django import forms

# My app imports
from actividades.models import *


class RechazarForm(ModelForm):
    class Meta:
        model = Actividad
        fields = ('motivo_rechazo', )


class EstadiaForm(ModelForm):
    class Meta:
        model = EstadiaPostdoctoral
        fields = ('nombre_actividad', 'lugar', 'fecha', 'resumen', 'archivo',)
        widgets = {
            "nombre_actividad": TextInput(attrs={
                "placeholder": "Nombre de la Actividad"
            }),
            "lugar": TextInput(attrs={
                "placeholder": "Lugar donde se realizo la Estadia"
            }),  # TextInput(attrs={})
            "fecha": TextInput(attrs={
                'class': 'datepicker',
                "placeholder": "Fecha en que se realizo la Estadia (YYYY-MM-DD)"
            }),
            "resumen": TextInput(attrs={
                'cols': 80,
                'rows': 20
            }),
            "archivo": "",
        }


class PublicacionForm(ModelForm):
    class Meta:
        model = Publicacion
        fields = ('nombre_actividad', 'lugar_publicacion', 'fecha', 'resumen', 'archivo')
        widgets = {
            "nombre_actividad": TextInput(attrs={
                "placeholder": "Nombre de la publicacion"
            }),
            "lugar_publicacion": TextInput(attrs={
                "placeholder": "Lugar donde se realizo la publicacion"
            }),
            "fecha": TextInput(attrs={
                'class': 'datepicker',
                "placeholder": "Fecha de Publicacion (YYYY-MM-DD)"
            }),
            "resumen": TextInput(attrs={
                "cols": 80,
                "rows": 20
            }),
            "archivo": "",
        }


class InvestigacionForm(ModelForm):
    class Meta:
        model = Investigacion
        fields = ('nombre_actividad', 'codigo', 'fecha', 'resumen', 'archivo',)
        widgets = {
            "nombre_actividad": TextInput(attrs={
                "placeholder": "Nombre de la Actividad"
            }),
            "codigo": TextInput(attrs={
                "placeholder": "Codigo de la Actividad"
            }),
            "fecha": TextInput(attrs={
                "class": "datepicker",
                "placeholder": "Fecha en que se inicio la Investigacion (YYYY-MM-DD)"
            }),
            "resumen": TextInput(attrs={
                "cols": 80,
                "rows": 20
            }),
            "archivo": ""
        }


class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = ("nombre_actividad", "editorial", "isbn", "fecha", "resumen", "archivo",)
        widgets = {
            "nombre_actividad": TextInput(attrs={
                "placeholder": "Nombre del Libro",
            }),
            "editorial": TextInput(attrs={
                "placeholder": "Nombre de la Editorial"
            }),
            "isbn": TextInput(attrs={
                "placeholder": "Codigo ISBN"
            }),
            "fecha": TextInput(attrs={
                'class': 'datepicker',
                "placeholder": "Fecha de Publicacion"
            }),
            "resumen": TextInput(attrs={
                "cols": 80,
                "rows": 20
            }),
            "archivo": ""
        }


class ConferenciaForm(ModelForm):
    class Meta:
        model = Conferencia
        fields = ('nombre_actividad', 'fecha', 'resumen', 'archivo')
        widgets = {
            "nombre_actividad": TextInput(attrs={
                "placeholder": "Nombre de la Conferencia",
            }),
            "fecha": TextInput(attrs={
                'class': 'datepicker',
                "placeholder": "Fecha en que se realizo la conferencia,"
            }),
            "resumen": TextInput(attrs={
                "cols": 80,
                "rows": 20
            }),
            "archivo": ""
        }


class PonenciaForm(ModelForm):
    class Meta:
        model = Ponencia
        fields = ('nombre_actividad', 'pais', 'fecha', 'resumen', 'archivo',)
        widgets = {
            "nombre_actividad": TextInput(attrs={
                "placeholder": "Nombre de la Actividad"
            }),
            "pais": forms.Select(attrs={
                "placeholder": "Pais donde se realizo la ponencia"
            }),
            "fecha": TextInput(attrs={
                "placeholder": "Fecha en que se realizo la ponencia",
                'class': 'datepicker',
            }),
            "resumen": "",
            "archivo": ""
        }


class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre_actividad', 'tipo', 'fecha', 'resumen', 'archivo',)
        widgets = {
            "nombre_actividad": TextInput(attrs={
                "placeholder": "Nombre del proyecto"
            }),
            "tipo": forms.Select(attrs={
                "placeholder": "Tipo del proyecto"
            }),
            "fecha": TextInput(attrs={
                'class': 'datepicker',
                "placeholder": "Fecha en que se realizo el proyecto",
            }),
        }


class PremioForm(ModelForm):
    class Meta:
        model = Premio
        fields = ('nombre_actividad', 'tipo', 'fecha', 'resumen', 'archivo',)
        widgets = {
            "nombre_actividad": TextInput(attrs={
                "placeholder": "Nombre del premio"
            }),
            "fecha": TextInput(attrs={
                'class': 'datepicker',
                "placeholder": "Fecha en que se recibio el premio",
            }),
        }


class TituloForm(ModelForm):
    class Meta:
        model = Titulo
        fields = ('info_titulo', 'centro_estudio', 'fecha', 'resumen', 'archivo',)
        widgets = {
            "info_titulo": forms.Select(attrs={
                "placeholder": "Titulo Adquirido"
            }),
            "centro_estudio": forms.Select(attrs={
                "placeholder": "Centro de Estudio donde Adquirio el titulo"
            }),
            "fecha": TextInput(attrs={
                'class': 'datepicker',
                "placeholder": "Fecha en que obtuvo el titulo",
            }),
        }


class IdiomaForm(ModelForm):
    # nombre = forms.ChoiceField(choices=LANGUAGES)

    class Meta:
        model = Idioma
        fields = ('nombre', 'nivel_hablado', 'nivel_escrito',)
        # widgets = {
        #     "nombre": TextInput(attrs={
        #         "class": "form-control"
        #     }),
        #     "nivel_hablado": TextInput(attrs={
        #         "placeholder": "Nivel de dominio hablado"
        #     }),
        #     "nivel_escrito": TextInput(attrs={
        #         "placeholder": "Nivel de dominio escrito"
        #     })
        # }
