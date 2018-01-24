from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Managers
from core.managers import PersonManager


# Create your models here.
# TODO: Crear un modelo base con, fecha_creacion, fecha_modificacion(ultima), modificado_por

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Notificaciones(models.Model):

    TIPOS = (
        ('', ''),
        ('', ''),
        ('', '')
    )
    tipo = models.CharField(max_length=1, choices=TIPOS, default='1')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return "Hello"
