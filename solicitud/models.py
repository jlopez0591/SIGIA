from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Solicitud(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    titulo = models.CharField(max_length=120)
    fecha_creacion = models.DateField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    resumen = models.TextField(max_length=500, blank=True)
    resuelto = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.fecha_creacion = timezone.now()
        self.fecha_modificacion = timezone.now()
        return super(Solicitud, self).save()

    def get_absolute_url(self):
        return reverse('solicitud:detalle', kwargs={'pk': self.pk})

    def resolver(self):
        self.resuelto = True
        self.save()

    def actualizar_fecha_modificacion(self):
        self.fecha_modificacion = timezone.now()
        self.save()


class Comentario(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(blank=True, null=True)
    resumen = models.TextField(max_length=500)

    def __str__(self):
        return '{0} - {1}'.format(self.usuario.get_full_name(), self.fecha)
