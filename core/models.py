from django.db import models
from django.contrib.auth.models import User, AbstractUser

from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField

from datetime import date
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Q
from django.urls import reverse
# Third party imports
from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django_countries.fields import CountryField

# This app imports
from .managers import PerfilManager

# Other apps
from ubicacion.models import Sede, FacultadInstancia, EscuelaInstancia, DepartamentoInstancia, CarreraInstancia
from actividades.models import Titulo


class User(AbstractUser):
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
    # Fechas
    fecha_nacimiento = models.DateField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)

    sexo = models.CharField(max_length=1, choices=GENERO, blank=True, null=True)

    # Informacion de cedula
    provincia = models.CharField(max_length=5, choices=PROVINCIAS, blank=True, null=True)
    clase = models.CharField(max_length=5, choices=CLASE, blank=True, null=True)
    tomo = models.CharField(max_length=5, blank=True, null=True)
    folio = models.CharField(max_length=5, blank=True, null=True)

    imagen = models.ImageField(upload_to='perfil/', blank=True)
    categoria = models.CharField(max_length=1, choices=CATEGORIAS, blank=True, null=True)
    pais = CountryField(blank=True, null=True)
    cod_profesor = models.CharField(max_length=120, blank=True, null=True)

    # Codigos de ubicacion
    cod_sede = models.CharField(max_length=2, blank=True, default='XX', null=True)
    cod_facultad = models.CharField(max_length=2, blank=True, default='XX', null=True)
    cod_escuela = models.CharField(max_length=2, blank=True, default='XX', null=True)
    cod_departamento = models.CharField(max_length=2, blank=True, default='XX', null=True)

    # Informacion de ubicacion
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, related_name='personal', blank=True,
                             null=True)
    facultad = models.ForeignKey(FacultadInstancia, on_delete=models.SET_NULL, related_name='personal',
                                 blank=True, null=True)
    departamento = models.ForeignKey(DepartamentoInstancia, blank=True, null=True, related_name='personal')
    escuela = models.ForeignKey(EscuelaInstancia, blank=True, null=True,
                                related_name='personal')

    history = AuditlogHistoryField()
    objects = PerfilManager()

    class Meta:
        permissions = (
            ('ver_perfil', 'Ver Perfil'),
        )
        verbose_name_plural = 'Perfiles'
        unique_together = ('provincia', 'clase', 'tomo', 'folio')

    def __str__(self):
        return self.usuario.username

    def save(self, *args, **kwargs):
        try:
            self.sede = Sede.objects.get(cod_sede=self.cod_sede)
        except ObjectDoesNotExist:
            pass
        try:
            self.facultad = FacultadInstancia.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad)
        except ObjectDoesNotExist:
            pass
        try:
            self.escuela = EscuelaInstancia.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad,
                                                        cod_escuela=self.cod_escuela)
        except ObjectDoesNotExist:
            pass
        try:
            self.departamento = DepartamentoInstancia.objects.get(cod_sede=self.cod_sede,
                                                                  cod_facultad=self.cod_facultad,
                                                                  cod_departamento=self.cod_departamento)
        except ObjectDoesNotExist:
            pass
        return super(User, self).save()

    def get_absolute_url(self):
        return reverse('perfil:publico', kwargs={'pk': self.pk})

    def nivel_academico(self):
        actividades = self.usuario.actividades.filter(clase='titulo')
        niveles = list()
        for actividad in actividades:
            titulo = Titulo.objects.get(pk=actividad.pk)
            nivel = titulo.info_titulo.nivel
            if nivel not in niveles:
                niveles.append(nivel)
        if 'doctorado' in niveles:
            return 'Doctor'
        elif 'maestria' in niveles:
            return 'Magister'
        elif 'postgrado' in niveles:
            return 'Postgrado'
        else:
            return 'Licenciado'

    def edad(self):
        if self.fecha_nacimiento:
            bd = date.today() - self.fecha_nacimiento
            return int(bd.days / 365)
        else:
            return "No tiene registrado una fecha de nacimiento"

    def tiempo_laborado(self):
        if self.fecha_inicio:
            tl = date.today() - self.fecha_inicio
            return int(tl.days / 365)
        else:
            return "No tiene registrado una fecha de inicio"


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
