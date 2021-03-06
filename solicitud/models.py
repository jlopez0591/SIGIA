from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog


class Solicitud(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    titulo = models.CharField(max_length=120)

    fecha_creacion = models.DateField(blank=True, null=True, auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True, auto_now=True)
    resumen = models.TextField(max_length=500, blank=True)
    resuelto = models.BooleanField(default=False)


    history = AuditlogHistoryField()

    class Meta:
        verbose_name_plural = 'Solicitudes'

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        return super(Solicitud, self).save()

    def get_absolute_url(self):
        return reverse('solicitud:detalle', kwargs={'pk': self.pk})

    def resolver(self):
        self.resuelto = True
        self.save()


class Comentario(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(blank=True, null=True, auto_now=True)
    resumen = models.TextField(max_length=500)

    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)
    history = AuditlogHistoryField()

    class Meta:
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return '{0} - {1}'.format(self.usuario.get_full_name(), self.fecha)


auditlog.register(Solicitud)
auditlog.register(Comentario)