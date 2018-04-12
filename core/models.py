from django.db import models
from django.contrib.auth.models import User

from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField


class Usuario(User):

    class Meta:
        proxy = True
    
    def __str__(self):
        return '{}, {} - {}'.format(self.last_name, self.first_name, self.perfil.cod_profesor)


class Notificacion(models.Model):
    history = AuditlogHistoryField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(blank=True, max_length=120)
    texto = models.CharField(max_length=120)
    url = models.URLField(blank=True)

    def __str__(self):
        return '{}-{}'.format(self.usuario.username, self.titulo)


def get_name(self):
    return '{} {}'.format(self.first_name, self.last_name)


User.add_to_class("__str__", get_name)

auditlog.register(Notificacion)
