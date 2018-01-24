# Python imports
from datetime import date

from django.apps import apps
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Q
from django.urls import reverse
# Third party imports
from django_countries.fields import CountryField

# This app imports
from .managers import PerfilManager


class Person(User):
    class Meta:
        proxy = True

    def codigos(self):
        codes = {
            'cod_sede': self.perfil.cod_sede,
            'cod_unidad': self.perfil.cod_unidad,
            'cod_seccion': self.perfil.cod_seccion
        }
        return codes


class Perfil(models.Model):
    CATEGORIAS = (
        ('1', 'Tiempo Completo'),
        ('2', 'Tiempo Parcial'),
    )
    GENERO = (
        ('h', 'Hombre'),
        ('m', 'Mujer')
    )
    NIVEL = (

    )
    PROVINCIAS = (
        ('00', '00'),
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('06', '06'),
        ('07', '07'),
        ('08', '08'),
        ('09', '09'),
    )
    CLASE = (
        ('00', '00'),
        ('N', 'N'),
        ('E', 'E'),
        ('EC', 'EC'),
        ('PE', 'PE'),
        ('AV', 'AV'),
        ('PI', 'PI'),
    )
    # Nombre
    primer_nombre = models.CharField(max_length=120, blank=True)
    segundo_nombre = models.CharField(max_length=120, blank=True)
    primer_apellido = models.CharField(max_length=120, blank=True)
    segundo_apellido = models.CharField(max_length=120, blank=True)

    nombre_completo = models.CharField(max_length=480, blank=True)

    # Fechas
    fecha_nacimiento = models.DateField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)

    # Info. Personal
    sexo = models.CharField(max_length=1, choices=GENERO)

    provincia = models.CharField(max_length=5, choices=PROVINCIAS, default='00')
    clase = models.CharField(max_length=5, default='00', choices=CLASE)
    tomo = models.CharField(max_length=5, default='000')
    folio = models.CharField(max_length=5, default='0000')

    cedula = models.CharField(max_length=20, blank=True)

    # Info. Profesor
    imagen = models.ImageField(upload_to='perfil/')
    categoria = models.CharField(max_length=1, choices=CATEGORIAS, blank=True, null=True)
    pais = CountryField(blank=True)

    # Info Ubicacion
    cod_sede = models.CharField(max_length=2, blank=True, default='XX')
    cod_unidad = models.CharField(max_length=2, blank=True, default='XX')
    cod_seccion = models.CharField(max_length=2, blank=True, default='XX')

    # Foreign Keys
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='perfil')
    # Considerar usar M2M Field y ArrayField de Postgres
    sede = models.ForeignKey('ubicacion.Sede', on_delete=models.SET_NULL, related_name='personal', blank=True,
                             null=True)
    unidad = models.ForeignKey('ubicacion.UnidadInstancia', on_delete=models.SET_NULL, related_name='personal',
                               blank=True, null=True)
    seccion = models.ForeignKey('ubicacion.SeccionInstancia',
                                limit_choices_to=Q(seccion__tipo='ES') | Q(seccion__tipo='DE'),
                                null=True,
                                on_delete=models.SET_NULL, related_name='personal', blank=True)

    objects = PerfilManager()

    class Meta:
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.nombre_completo + str(self.usuario.pk)

    def save(self, *args, **kwargs):
        self.seccion = self.asignar_ubicacion()
        self.cedula = self.armar_cedula()
        self.nombre_completo = '{} {} {} {}'.format(self.primer_nombre, self.segundo_nombre, self.primer_apellido,
                                                    self.segundo_apellido)
        return super(Perfil, self).save()

    def get_unidad(self):
        return self.seccion.ubicacion

    def asignar_ubicacion(self):
        seccion_model = apps.get_model('ubicacion', 'SeccionInstancia')
        try:
            return seccion_model.objects.get(cod_sede=self.cod_sede, cod_unidad=self.cod_unidad,
                                             cod_seccion=self.cod_seccion)
        except ObjectDoesNotExist:
            return None

    def armar_cedula(self):
        return '{}-{}-{}-{}'.format(self.provincia, self.clase, self.tomo, self.folio)

    def get_absolute_url(self):
        return reverse('perfil:publico', kwargs={'pk': self.pk})

    def codigos(self):
        codes = {
            'cod_sede': self.cod_sede,
            'cod_unidad': self.cod_unidad,
            'cod_seccion': self.cod_seccion
        }
        return codes

    def edad(self):
        bd = date.today() - self.fecha_nacimiento
        return int(bd.days / 365)

    def tiempo_laborado(self):
        tl = date.today() - self.fecha_inicio
        return int(tl.days / 365)
