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


class Aula(models.Model):
    AULA = '1'
    LABORATORIO = '2'
    OFICINA = '3'
    TIPOS = (
        (AULA, 'Aula'),
        (LABORATORIO, 'Laboratorio'),
        (OFICINA, 'Oficina'),
    )
    numero = models.CharField(max_length=5)
    tipo = models.CharField(choices=TIPOS, max_length=1)

    ubicacion = models.ForeignKey('ubicacion.UnidadInstancia', null=True, blank=True, on_delete=models.CASCADE)
    cod_sede = models.CharField(max_length=2, blank=True)
    cod_unidad = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.numero

    def save(self, *args, **kwargs):
        try:
            self.ubicacion = Ubicacion.objects.get(cod_sede=self.cod_sede, cod_unidad=self.cod_unidad)
        except:
            pass
        return super(Aula, self).save()


class Equipo(models.Model):
    etiqueta = models.CharField(max_length=120, unique=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, related_name='equipos')
    cod_sede = models.CharField(max_length=2, blank=True)
    cod_unidad = models.CharField(max_length=2, blank=True)
    observaciones = models.TextField(max_length=500, blank=True)

    aula = models.ForeignKey(Aula, on_delete=models.SET_NULL, null=True, blank=True)
    ubicacion = models.ForeignKey('ubicacion.UnidadInstancia', on_delete=models.CASCADE, blank=True, null=True, related_name='equipos')

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
