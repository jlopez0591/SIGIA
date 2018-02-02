from django.db import models
from django.contrib.auth.models import User


class Notificacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(blank=True, max_length=120    )
    url = models.URLField(blank=True)

    def __str__(self):
        return '{}-{}'.format(self.usuario.get_full_name(), self.titulo)
