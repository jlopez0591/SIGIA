from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Q
from django.urls import reverse

from .managers import (CarreraInstanciaManager, CarreraManager,
                       SeccionInstanciaManager, SeccionManager, SedeManager,
                       UnidadInstanciaManager, UnidadManager)


class Sede(models.Model):
    CAMPUS = 'CU'
    CENTRO_REGIONAL = 'CR'
    EXTENSION = 'EX'
    PROYECTO_ANEXO = 'PA'

    TIPOS = (
        (CAMPUS, 'Campus'),
        (CENTRO_REGIONAL, 'Centro Regional'),
        (EXTENSION, 'Extension'),
        (PROYECTO_ANEXO, 'Proyecto Anexo'),
    )
    objects = SedeManager()

    cod_sede = models.CharField(max_length=2, unique=True)
    nombre = models.CharField(max_length=120, unique=True)
    tipo = models.CharField(max_length=2, choices=TIPOS, default='PA')
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Sedes'

    def __str__(self):
        return '{} - {}'.format(self.cod_sede, self.nombre)

    def get_absolute_url(self):
        return reverse('ubicacion:sede', kwargs={
            'cod_sede': self.cod_sede
        })


class Unidad(models.Model):
    '''
        Define la informacion de una facultad, estas pueden ser
        Facultades, vicerrectorias, institutos, asociaciones o coordinaciones.
        Para este sistema solo se utilizara Facultades y Coordinaciones.
    '''
    FACULTAD = 'FA'
    VICERRECTORIA = 'VI'

    TIPOS = (
        (FACULTAD, 'Facultad'),
        (VICERRECTORIA, 'Vicerrectoria'),
    )
    objects = UnidadManager()

    cod_facultad = models.CharField(max_length=2, unique=True)
    nombre = models.CharField(max_length=120, unique=True)
    tipo = models.CharField(max_length=2, choices=TIPOS, default=FACULTAD)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Informacion de Facultades y Organizaciones'

    def __str__(self):
        return '{} - {}'.format(self.cod_facultad, self.nombre)

    def get_absolute_url(self):
        pass


class Seccion(models.Model):
    ESCUELA = 'ES'
    DEPARTAMENTO = 'DE'
    COMISION = 'CO'
    DECANATO = 'DC'

    TIPOS = (
        (ESCUELA, 'Escuela'),
        (DEPARTAMENTO, 'Departamento'),
        (COMISION, 'Comision'),
        (DECANATO, 'Decanato'),
    )
    objects = SeccionManager()

    cod_facultad = models.CharField(max_length=2)
    cod_escuela = models.CharField(max_length=2)
    nombre = models.CharField(max_length=120)
    tipo = models.CharField(max_length=2, choices=TIPOS, default=ESCUELA)
    activo = models.BooleanField(default=True)
    facultad = models.ForeignKey(Unidad, limit_choices_to=Q(tipo='FA'), blank=True, null=True,
                                 on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('cod_escuela', 'cod_facultad')
        verbose_name_plural = 'Informacion de Escuelas, Direcciones, Departamentos y Organizaciones'

    def __str__(self):
        return '{} - {}'.format(self.cod_facultad, self.cod_escuela)

    def save(self, *args, **kwargs):
        try:
            self.facultad = Unidad.objects.get(cod_facultad=self.cod_facultad)
        except ObjectDoesNotExist:
            pass
        return super(Seccion, self).save()


class Departamento(models.Model):
    cod_facultad = models.CharField(max_length=2)
    cod_departamento = models.CharField(max_length=2)

    def __str__(self):
        return '{} - {}'.format(self.cod_facultad, self.cod_departamento)


class Carrera(models.Model):
    REGULAR = 'R'
    POSTGRADO = 'P'
    MAESTRIA = 'M'
    DOCTORADO = 'D'
    CURSO_DIPLOMADO = 'C'

    TIPOS = (
        (REGULAR, 'Regular'),
        (POSTGRADO, 'Postgrado'),
        (MAESTRIA, 'Maestria'),
        (DOCTORADO, 'Doctorado'),
        (CURSO_DIPLOMADO, 'Curso / Diplomado'),
    )
    objects = CarreraManager()

    facultad = models.ForeignKey(Unidad, on_delete=models.CASCADE, limit_choices_to=(Q(tipo='FA')),
                                 blank=True, null=True)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, limit_choices_to=(Q(tipo='ES')), blank=True,
                                null=True)
    cod_facultad = models.CharField(max_length=2)
    cod_escuela = models.CharField(max_length=2)
    cod_carrera = models.CharField(max_length=2)

    nombre = models.CharField(max_length=120)
    activo = models.BooleanField(default=True)
    tipo = models.CharField(max_length=1, choices=TIPOS, default=REGULAR)

    class Meta:
        unique_together = ('cod_facultad', 'cod_escuela', 'cod_carrera')
        verbose_name_plural = 'informacion de Carreras'

    def __str__(self):
        return '{}-{}-{}'.format(self.cod_facultad, self.cod_escuela, self.cod_carrera)

    def save(self, *args, **kwargs):
        self.facultad = Unidad.objects.get(cod_facultad=self.cod_facultad)
        self.seccion = Seccion.objects.get(cod_facultad=self.cod_facultad, cod_escuela=self.cod_escuela)
        return super(Carrera, self).save()


class UnidadInstancia(models.Model):
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, related_name='facultades', blank=True, null=True)
    facultad = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='instancias', blank=True, null=True)
    activo = models.BooleanField(default=True)

    cod_sede = models.CharField(max_length=2)
    cod_facultad = models.CharField(max_length=2)

    decano = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    objects = UnidadInstanciaManager()

    class Meta:
        unique_together = ('cod_sede', 'cod_facultad')
        verbose_name_plural = 'Instancia de Facultad u Organizacion'

    def __str__(self):
        return '{}-{}'.format(self.cod_sede, self.cod_facultad)

    def save(self, *args, **kwargs):
        try:
            self.sede = Sede.objects.get(cod_sede=self.cod_sede)
            self.facultad = Unidad.objects.get(cod_facultad=self.cod_facultad)
        except ObjectDoesNotExist:
            pass
        return super(UnidadInstancia, self).save()

    def get_absolute_url(self):
        return reverse('ubicacion:facultad', kwargs={
            'cod_sede': self.cod_sede,
            'cod_facultad': self.cod_facultad
        })


class SeccionInstancia(models.Model):
    objects = SeccionInstanciaManager()

    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, related_name='secciones', blank=True, null=True)
    facultad = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='secciones', blank=True, null=True)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name='secciones', blank=True, null=True)

    cod_sede = models.CharField(max_length=2)
    cod_facultad = models.CharField(max_length=2)
    cod_escuela = models.CharField(max_length=2)

    ubicacion = models.ForeignKey(UnidadInstancia, on_delete=models.CASCADE, related_name='secciones', blank=True,
                                  null=True, limit_choices_to=(Q(facultad__tipo='FA')) | Q(facultad__tipo='6'))
    activo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('cod_sede', 'cod_facultad', 'cod_escuela')
        verbose_name_plural = 'Instancia de Escuela, Direccion, Departamento u Organizacion'

    def __str__(self):
        return '{}-{}-{}'.format(self.cod_sede, self.cod_facultad, self.cod_escuela)

    def save(self, *args, **kwargs):
        try:
            self.sede = Sede.objects.get(cod_sede=self.cod_sede)
            self.facultad = Unidad.objects.get(cod_facultad=self.cod_facultad)
            self.seccion = Seccion.objects.get(cod_facultad=self.cod_facultad, cod_escuela=self.cod_escuela)
            self.ubicacion = UnidadInstancia.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad)
        except ObjectDoesNotExist:
            pass
        return super(SeccionInstancia, self).save()

    def get_absolute_url(self):
        return reverse('ubicacion:seccion', kwargs={
            'cod_sede': self.cod_sede,
            'cod_facultad': self.cod_facultad,
            'cod_escuela': self.cod_escuela
        })


class DepartamentoInstancia(models.Model):
    cod_sede = models.CharField(max_length=2)
    cod_facultad = models.CharField(max_length=2)
    cod_departamento = models.CharField(max_length=2)

    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, blank=True, null=True)
    facultad = models.ForeignKey(Unidad, on_delete=models.CASCADE, blank=True, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, blank=True, null=True)
    ubicacion = models.ForeignKey(UnidadInstancia, on_delete=models.CASCADE, blank=True, null=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return '{}-{}-{}'.format(self.cod_sede, self.cod_facultad, self.cod_departamento)

    def save(self, *args, **kwargs):
        try:
            self.sede = Sede.objects.get(cod_sede=self.cod_sede)
            self.facultad = Unidad.objects.get(cod_facultad=self.cod_facultad)
            self.departamento = Departamento.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad,
                                                         cod_departamento=self.cod_departamento)
            self.ubicacion = UnidadInstancia.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad)
        except ObjectDoesNotExist:
            pass


class CarreraInstancia(models.Model):
    objects = CarreraInstanciaManager()

    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, blank=True, null=True, related_name='carreras')
    facultad = models.ForeignKey(Unidad, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name='carrera_instancia')
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='carrera_instancia')
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='carrera_instancia')

    ubicacion = models.ForeignKey(SeccionInstancia, on_delete=models.CASCADE, blank=True, null=True,
                                  limit_choices_to=Q(seccion__tipo='ES'), related_name='carreras')

    cod_sede = models.CharField(max_length=2)
    cod_facultad = models.CharField(max_length=2)
    cod_escuela = models.CharField(max_length=2)
    cod_carrera = models.CharField(max_length=2)

    activo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('cod_sede', 'cod_facultad', 'cod_escuela', 'cod_carrera')
        verbose_name_plural = 'Instancia de Carrera'

    def __str__(self):
        return '{}-{}-{}-{}'.format(self.cod_sede, self.cod_facultad, self.cod_escuela, self.cod_carrera)

    def save(self, *args, **kwargs):
        try:
            self.sede = Sede.objects.get(cod_sede=self.cod_sede)
            self.facultad = Unidad.objects.get(cod_facultad=self.cod_facultad)
            self.seccion = Seccion.objects.get(cod_facultad=self.cod_facultad, cod_escuela=self.cod_escuela)
            self.carrera = Carrera.objects.get(cod_facultad=self.cod_facultad, cod_escuela=self.cod_escuela,
                                               cod_carrera=self.cod_carrera)
            self.ubicacion = SeccionInstancia.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad,
                                                          cod_escuela=self.cod_escuela)
        except ObjectDoesNotExist:
            pass
        return super(CarreraInstancia, self).save()

    def get_absolute_url(self):
        return reverse('ubicacion:carrera', kwargs={
            'cod_sede': self.cod_sede,
            'cod_facultad': self.cod_facultad,
            'cod_escuela': self.cod_escuela,
            'cod_carrera': self.cod_carrera
        })

    def nombre_completo(self):
        return '{} - {} - {} - {}'.format(self.sede.nombre, self.facultad.nombre, self.seccion.nombre,
                                          self.carrera.nombre)
