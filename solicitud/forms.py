# django
from django import forms
from django.forms import ModelForm, TextInput

# app
from solicitud.models import Solicitud, Comentario


class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = ('titulo', 'resumen')
        widgets = {
            "titulo": TextInput(attrs={
                'placeholder': 'Nombre de Solicitud',
                'class': 'form-control'
            }),
            "resumen": TextInput(attrs={
                'placeholder': 'Descripcion de su solicitud'
            })
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('resumen',)
        widgets = {}
