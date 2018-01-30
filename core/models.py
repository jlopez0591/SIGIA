from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Notificaciones(TimeStampedModel):
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
        return '{} - {}'.format(self.usuario.get_full_name(), self.tipo)
