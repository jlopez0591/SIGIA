from django.db import models
from django.urls import reverse

from ubicacion.models import FacultadInstancia

from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField


# Create your models here.
class Fabricante(models.Model):
    history = AuditlogHistoryField()
    nombre = models.CharField(max_length=120, unique=True)
    url = models.URLField(blank=True)

    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('inventario:fabricante-detalle', kwargs={
            'pk': self.pk
        })


class Categoria(models.Model):
    history = AuditlogHistoryField()
    nombre = models.CharField(max_length=120, unique=True)

    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('inventario:categoria-detalle', kwargs={
            'pk': self.pk
        })


class Modelo(models.Model):
    history = AuditlogHistoryField()
    nombre = models.CharField(max_length=120, unique=True)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, related_name='modelos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='modelos')
    url = models.URLField(blank=True)

    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)

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
    history = AuditlogHistoryField()
    numero = models.CharField(max_length=5)
    tipo = models.CharField(choices=TIPOS, max_length=1)

    ubicacion = models.ForeignKey(FacultadInstancia, null=True, blank=True, on_delete=models.CASCADE)
    cod_sede = models.CharField(max_length=2, blank=True)
    cod_facultad = models.CharField(max_length=2, blank=True)

    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.numero

    def equipos_categoria(self):
        """
        Genera diccionario de equipos con llave por categoria a la que pertenecen (eg. Computadoras)
        :return:
        """
        equipos = dict()
        qs = self.equipo_set.all()
        for equipo in qs:
            nombre = equipo.modelo.categoria.nombre
            if nombre in equipos:
                equipos[nombre].append(equipo)
            else:
                equipos[nombre] = [equipo]
        return equipos

    def save(self, *args, **kwargs):
        try:
            self.ubicacion = FacultadInstancia.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad)
        except:
            pass
        return super(Aula, self).save()


class Equipo(models.Model):
    history = AuditlogHistoryField()
    etiqueta = models.CharField(max_length=120, unique=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, related_name='equipos')
    cod_sede = models.CharField(max_length=2, blank=True)
    cod_facultad = models.CharField(max_length=2, blank=True)
    observaciones = models.TextField(max_length=500, blank=True)

    aula = models.ForeignKey(Aula, on_delete=models.SET_NULL, null=True, blank=True)
    ubicacion = models.ForeignKey(FacultadInstancia, on_delete=models.CASCADE, blank=True, null=True,
                                  related_name='equipos')

    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return 'Facultad:{}, Equipo:{} Etiqueta:{}'.format(self.ubicacion, self.modelo, self.etiqueta)

    def get_absolute_url(self):
        return reverse('inventario:detalle-equipo', kwargs={
            'pk': self.pk
        })

    def save(self, *args, **kwargs):
        try:
            self.ubicacion = FacultadInstancia.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad)
        except:
            pass
        return super(Equipo, self).save()


auditlog.register(Fabricante)
auditlog.register(Categoria)
auditlog.register(Modelo)
auditlog.register(Aula)
auditlog.register(Equipo)
