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
from ubicacion.models import Sede, UnidadInstancia, SeccionInstancia, CarreraInstancia
from actividades.models import Titulo


def imagen_pergil_location(instance, filename):
    pass


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
    primer_nombre = models.CharField(max_length=120, blank=True)
    segundo_nombre = models.CharField(max_length=120, blank=True)
    primer_apellido = models.CharField(max_length=120, blank=True)
    segundo_apellido = models.CharField(max_length=120, blank=True)

    nombre_completo = models.CharField(max_length=480, blank=True)

    fecha_nacimiento = models.DateField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)

    sexo = models.CharField(max_length=1, choices=GENERO, blank=True, null=True)

    provincia = models.CharField(max_length=5, choices=PROVINCIAS, default='00', blank=True, null=True)
    clase = models.CharField(max_length=5, default='00', choices=CLASE, blank=True, null=True)
    tomo = models.CharField(max_length=5, default='000', blank=True, null=True)
    folio = models.CharField(max_length=5, default='0000', blank=True, null=True)

    imagen = models.ImageField(upload_to='perfil/', blank=True)
    categoria = models.CharField(max_length=1, choices=CATEGORIAS, blank=True, null=True)
    pais = CountryField(blank=True, null=True)
    cod_profesor = models.CharField(max_length=120, blank=True, null=True)

    cod_sede = models.CharField(max_length=2, blank=True, default='XX', null=True)
    cod_facultad = models.CharField(max_length=2, blank=True, default='XX', null=True)
    cod_escuela = models.CharField(max_length=2, blank=True, default='XX', null=True)
    cod_departamento = models.CharField(max_length=2, blank=True, default='XX', null=True)

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='perfil')
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, related_name='personal', blank=True,
                             null=True)
    facultad = models.ForeignKey(UnidadInstancia, on_delete=models.SET_NULL, related_name='personal',
                                 blank=True, null=True)
    departamento = models.ForeignKey(SeccionInstancia, blank=True, null=True, related_name='personal',
                                     limit_choices_to=Q(seccion__tipo='DE'),
                                     )
    escuela = models.ForeignKey(SeccionInstancia, blank=True, null=True,
                                limit_choices_to=Q(seccion__tipo='ES'),
                                related_name='administrativos')

    history = AuditlogHistoryField()
    objects = PerfilManager()

    class Meta:
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.usuario.username

    def save(self, *args, **kwargs):
        try:
            self.sede = Sede.objects.get(cod_sede=self.cod_sede)
            self.facultad = UnidadInstancia.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad)
            self.escuela = SeccionInstancia.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad,
                                                        cod_escuela=self.cod_escuela)
            self.departamento = SeccionInstancia.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad,
                                                             cod_escuela=self.cod_departamento)
        except ObjectDoesNotExist:
            pass
        return super(Perfil, self).save()

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


auditlog.register(Perfil)