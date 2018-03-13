from django.db import models
from django.contrib.auth.models import User

from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField


class Notificacion(models.Model):
    history = AuditlogHistoryField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(blank=True, max_length=120)
    texto = models.CharField(max_length=120)
    url = models.URLField(blank=True)

    def __str__(self):
        return '{}-{}'.format(self.usuario.username, self.titulo)


auditlog.register(Notificacion)
