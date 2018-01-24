from django.db import models
from django.urls import reverse

from ubicacion.models import UnidadInstancia as Ubicacion


# Create your models here.
class Fabricante(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('inventario:fabricante-detalle', kwargs={
            'pk': self.pk
        })


class Categoria(models.Model):
    nombre = models.CharField(max_length=120, unique=True)


    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('inventario:categoria-detalle', kwargs={
            'pk': self.pk
        })


class Modelo(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, related_name='modelos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='modelos')
    url = models.URLField(blank=True)

    def __str__(self):
        return '{} - {} {}'.format(self.categoria.nombre, self.fabricante.nombre, self.nombre)

    def get_absolute_url(self):
        return reverse('inventario:modelo-detalle', kwargs={
            'pk': self.pk
        })


class Equipo(models.Model):
    etiqueta = models.CharField(max_length=120, unique=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, related_name='equipos')
    cod_sede = models.CharField(max_length=2, blank=True)
    cod_unidad = models.CharField(max_length=2, blank=True)
    observaciones = models.TextField(max_length=500, blank=True)


    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, blank=True, null=True, related_name='equipos')

    def __str__(self):
        return '{} {} {}'.format(self.ubicacion, self.modelo, self.etiqueta)

    def get_absolute_url(self):
        return reverse('inventario:equipo-detalle', kwargs={
            'pk': self.pk
        })

    def save(self, *args, **kwargs):
        try:
            self.ubicacion = Ubicacion.objects.get(cod_sede=self.cod_sede, cod_unidad=self.cod_unidad)
        except:
            pass
        return super(Equipo, self).save()
