# Python imports
import logging

# Django imports
from django.apps import apps
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.urls import reverse

# My imports
from .managers import (CarreraInstanciaManager, CarreraManager,
                       SeccionInstanciaManager, SeccionManager, SedeManager,
                       UnidadInstanciaManager, UnidadManager)

logger = logging.getLogger(__name__)


# Create your models here.
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

    def get_unidades_tipo_count(self):
        """
        Cuenta las uniadades por tipo y las guarda en un diccionario
        :return: Cantidad de unidades por tipo en diccionario python
        """
        unidades = self.unidades.all()
        unidad_dict = {}
        for instancia in unidades:
            tipo = instancia.unidad.get_tipo_display()
            if tipo in unidad_dict:
                unidad_dict[tipo] += 1
            else:
                unidad_dict[tipo] = 1
        return unidad_dict

    def get_carreras_tipo_count(self):
        """
        Realiza conteo de las carreras por tipo
        :return: Conteo de carreras por tipo
        """
        carreras = self.carreras.all()
        conteo = {}
        for instancia in carreras:
            tipo = instancia.carrera.get_tipo_display()
            if tipo in conteo:
                conteo[tipo] += 1
            else:
                conteo[tipo] = 1
        return conteo

    def get_profesores_unidad_count(self):
        profesores = self.personal.profesores()
        conteo = {}
        for profesor in profesores:
            cs = profesor.cod_sede
            cf = profesor.cod_unidad
            facultad = UnidadInstancia.objects.get(cod_sede=cs, cod_unidad=cf)
            ubicacion = facultad.unidad.nombre
            if ubicacion in conteo:
                conteo[ubicacion] += 1
            else:
                conteo[ubicacion] = 1
        return conteo

    def get_estudiante_facultad_count(self):
        conteo = {}
        estudiantes = self.estudiantes.all()
        for estudiante in estudiantes:
            cs = estudiante.cod_sede
            cf = estudiante.cod_unidad  # Codigo de Facultad
            nombre_facultad = UnidadInstancia.objects.get(cod_sede=cs, cod_unidad=cf).unidad.nombre.title()
            if nombre_facultad in conteo:
                conteo[nombre_facultad] += 1
            else:
                conteo[nombre_facultad] = 1
        return conteo


class Unidad(models.Model):
    '''
        Define la informacion de una unidad, estas pueden ser
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

    cod_unidad = models.CharField(max_length=2, unique=True)
    nombre = models.CharField(max_length=120, unique=True)
    tipo = models.CharField(max_length=2, choices=TIPOS, default=FACULTAD)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Informacion de Facultades y Organizaciones'

    def __str__(self):
        return '{} - {}'.format(self.cod_unidad, self.nombre)

    def get_absolute_url(self):
        pass

    def natural_key(self):
        return (self.cod_unidad,)


class Seccion(models.Model):
    '''
        Define la informacion de las secciones, estan pueden ser
        Escuelas:
        Departamentos:
        Coordinaciones:
        Decanatos:
        Organizaciones:
    '''
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

    cod_unidad = models.CharField(max_length=2)
    cod_seccion = models.CharField(max_length=2)
    nombre = models.CharField(max_length=120)
    tipo = models.CharField(max_length=2, choices=TIPOS, default=ESCUELA)
    activo = models.BooleanField(default=True)
    unidad = models.ForeignKey(Unidad, limit_choices_to=Q(tipo='FA'), blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('cod_seccion', 'cod_unidad')
        verbose_name_plural = 'Informacion de Escuelas, Direcciones, Departamentos y Organizaciones'

    def __str__(self):
        return '{} - {}'.format(self.cod_unidad, self.cod_seccion)

    def save(self, *args, **kwargs):
        self.unidad = Unidad.objects.get(cod_unidad=self.cod_unidad)
        return super(Seccion, self).save()


class Departamento(models.Model):
    cod_unidad = models.CharField(max_length=2)
    cod_departamento = models.CharField(max_length=2)


class Carrera(models.Model):
    '''
        Almacena la informacion de las carreras dentro de las secciones de tipo escuela
    '''
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

    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, limit_choices_to=(Q(tipo='FA')),
                               blank=True, null=True)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, limit_choices_to=(Q(tipo='ES')), blank=True,
                                null=True)
    cod_unidad = models.CharField(max_length=2)
    cod_seccion = models.CharField(max_length=2)
    cod_carrera = models.CharField(max_length=2)

    nombre = models.CharField(max_length=120)
    activo = models.BooleanField(default=True)
    tipo = models.CharField(max_length=1, choices=TIPOS, default=REGULAR)

    class Meta:
        unique_together = ('cod_unidad', 'cod_seccion', 'cod_carrera')
        verbose_name_plural = 'informacion de Carreras'

    def __str__(self):
        return '{}-{}-{}'.format(self.cod_unidad, self.cod_seccion, self.cod_carrera)

    def save(self, *args, **kwargs):
        self.unidad = Unidad.objects.get(cod_unidad=self.cod_unidad)
        self.seccion = Seccion.objects.get(cod_unidad=self.cod_unidad, cod_seccion=self.cod_seccion)
        return super(Carrera, self).save()

    def natural_key(self):
        return (self.cod_unidad, self.cod_seccion, self.cod_carrera)


class UnidadInstancia(models.Model):
    '''
        Describe y actua como una de las ubicaciones dentro de la institucion
        Obtiene su informacion mediante las variables sede y unidad.
    '''
    objects = UnidadInstanciaManager()

    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, related_name='unidades', blank=True, null=True)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='instancias', blank=True, null=True)
    activo = models.BooleanField(default=True)

    cod_sede = models.CharField(max_length=2)
    cod_unidad = models.CharField(max_length=2)

    decano = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('cod_sede', 'cod_unidad')
        verbose_name_plural = 'Instancia de Facultad u Organizacion'

    def __str__(self):
        return '{}-{}'.format(self.cod_sede, self.cod_unidad)

    def save(self, *args, **kwargs):
        try:
            self.sede = Sede.objects.get(cod_sede=self.cod_sede)
            self.unidad = Unidad.objects.get(cod_unidad=self.cod_unidad)
        except:
            # TODO: Add sys.exc_info()[0]
            logger.error(
                'Hubo un error en la instancia con codigo {}-{}\nError: '.format(self.cod_sede, self.cod_unidad))
        return super(UnidadInstancia, self).save()

    def get_absolute_url(self):
        return reverse('ubicacion:unidad', kwargs={
            'cod_sede': self.cod_sede,
            'cod_unidad': self.cod_unidad
        })

    def get_recursos_modelo_count(self):
        recursos = self.equipos.all()
        conteo = {}
        for equipo in recursos:
            modelo = equipo.modelo.nombre
            if modelo in conteo:
                conteo[modelo] += 1
            else:
                conteo[modelo] = 1
        return conteo

    def get_recursos_tipo_count(self):
        recursos = self.equipos.all()
        conteo = {}
        for equipo in recursos:
            tipo = equipo.modelo.categoria.nombre
            if tipo in conteo:
                conteo[tipo] += 1
            else:
                conteo[tipo] = 1
        return conteo


class SeccionInstancia(models.Model):
    '''
            Describe y actua como una de las secciones dentro de una unidad
            Obtiene su informacion mediante las variables sede, unidad y seccion
    '''
    objects = SeccionInstanciaManager()

    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, related_name='secciones', blank=True, null=True)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='secciones', blank=True, null=True)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name='secciones', blank=True, null=True)

    cod_sede = models.CharField(max_length=2)
    cod_unidad = models.CharField(max_length=2)
    cod_seccion = models.CharField(max_length=2)

    ubicacion = models.ForeignKey(UnidadInstancia, on_delete=models.CASCADE, related_name='secciones', blank=True,
                                  null=True, limit_choices_to=(Q(unidad__tipo='FA')) | Q(unidad__tipo='6'))
    activo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('cod_sede', 'cod_unidad', 'cod_seccion')
        verbose_name_plural = 'Instancia de Escuela, Direccion, Departamento u Organizacion'

    def __str__(self):
        return '{}-{}-{}'.format(self.cod_sede, self.cod_unidad, self.cod_seccion)

    def save(self, *args, **kwargs):
        try:
            self.sede = Sede.objects.get(cod_sede=self.cod_sede)
            self.unidad = Unidad.objects.get(cod_unidad=self.cod_unidad)
            self.seccion = Seccion.objects.get(cod_unidad=self.cod_unidad, cod_seccion=self.cod_seccion)
            self.ubicacion = UnidadInstancia.objects.get(cod_sede=self.cod_sede, cod_unidad=self.cod_unidad)
        except:
            logger.error(
                'Hubo un error al asignar los datos para la instancia {}-{}-{}'.format(self.cod_sede, self.cod_unidad,
                                                                                       self.cod_seccion))
        return super(SeccionInstancia, self).save()

    def get_absolute_url(self):
        return reverse('ubicacion:seccion', kwargs={
            'cod_sede': self.cod_sede,
            'cod_unidad': self.cod_unidad,
            'cod_seccion': self.cod_seccion
        })

    def get_estudiante_count(self):
        return self.estudiantes.activos().count()


class CarreraInstancia(models.Model):
    '''
        Describe y actua como una de las carreras dentro de una seccion
        Obtiene su informacion mediante las variables sede, unidad, seccion y carrera.
    '''
    objects = CarreraInstanciaManager()

    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, blank=True, null=True, related_name='carreras')
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, blank=True, null=True,
                               related_name='carrera_instancia')
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='carrera_instancia')
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='carrera_instancia')

    facultad = models.ForeignKey(UnidadInstancia, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name='carreras')
    ubicacion = models.ForeignKey(SeccionInstancia, on_delete=models.CASCADE, blank=True, null=True,
                                  limit_choices_to=Q(seccion__tipo='ES'), related_name='carreras')

    cod_sede = models.CharField(max_length=2)
    cod_unidad = models.CharField(max_length=2)
    cod_seccion = models.CharField(max_length=2)
    cod_carrera = models.CharField(max_length=2)

    activo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('cod_sede', 'cod_unidad', 'cod_seccion', 'cod_carrera')
        verbose_name_plural = 'Instancia de Carrera'

    def __str__(self):
        return '{}-{}-{}-{}'.format(self.cod_sede, self.cod_unidad, self.cod_seccion, self.cod_carrera)

    def save(self, *args, **kwargs):
        try:
            self.sede = Sede.objects.get(cod_sede=self.cod_sede)
        except:
            logger.error('Hubo un error al encontrar la unidad para {}-{}'.format(self.cod_sede, self.cod_unidad))
        try:
            self.unidad = Unidad.objects.get(cod_unidad=self.cod_unidad)
        except:
            logger.error('Hubo un error al encontrar la unidad para {}'.format(self.cod_unidad))
        try:
            self.seccion = Seccion.objects.get(cod_unidad=self.cod_unidad, cod_seccion=self.cod_seccion)
        except:
            logger.error('Hubo un error al encontrar la seccion para {}-{}'.format(self.cod_unidad, self.cod_seccion))
        try:
            self.carrera = Carrera.objects.get(cod_unidad=self.cod_unidad, cod_seccion=self.cod_seccion,
                                               cod_carrera=self.cod_carrera)

        except:
            logger.error('Hubo un error al encontrar la carrera para {}-{}-{}'.format(self.cod_unidad, self.cod_seccion,
                                                                                      self.cod_carrera))
        try:
            self.ubicacion = SeccionInstancia.objects.get(cod_sede=self.cod_sede, cod_unidad=self.cod_unidad,
                                                          cod_seccion=self.cod_seccion)
        except:
            logger.error('Hubo un error al encontrar la sede para {}-{}-{}-{}'.format(self.cod_sede, self.cod_unidad,
                                                                                      self.cod_seccion,
                                                                                      self.cod_carrera))

        return super(CarreraInstancia, self).save()

    def get_absolute_url(self):
        return reverse('ubicacion:carrera', kwargs={
            'cod_sede': self.cod_sede,
            'cod_unidad': self.cod_unidad,
            'cod_seccion': self.cod_seccion,
            'cod_carrera': self.cod_carrera
        })

    def nombre_completo(self):
        return '{} - {} - {} - {}'.format(self.sede.nombre, self.unidad.nombre, self.seccion.nombre,
                                          self.carrera.nombre)
