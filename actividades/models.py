import logging

from django.conf.global_settings import LANGUAGES
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Third party imports
from django_countries.fields import CountryField
from polymorphic.models import PolymorphicModel

# Utilities and helpers
from .managers import ActividadManager

# Other apps import
from ubicacion.models import SeccionInstancia
from perfiles.models import Perfil

logger = logging.getLogger(__name__)


# Create your models here.
class Actividad(PolymorphicModel):
    ESTADIA = 'estadia_postdoctoral'
    PUBLICACION = 'publicacion'
    INVESTIGACION = 'investigacion'
    LIBRO = 'libro'
    CONFERENCIA = 'conferencia'
    PONENCIA = 'ponencia'
    PROYECTO = 'proyecto'
    PREMIO = 'premio'
    IDIOMA = 'idioma'
    TITULO = 'titulo'
    OTRO = 'otro'

    CLASES = (
        (ESTADIA, 'Estadia Postdoctoral'),
        (PUBLICACION, 'Publicacion'),
        (INVESTIGACION, 'Investigacion'),
        (LIBRO, 'Libro'),
        (CONFERENCIA, 'Conferencia'),
        (PONENCIA, 'Ponencia'),
        (PROYECTO, 'Proyecto'),
        (PREMIO, 'Premio'),
        (IDIOMA, 'Idioma'),
        (TITULO, 'Titulo'),
        (OTRO, 'Otro'),
    )

    ESPERA = 'espera'
    RECHAZADO = 'rechazado'
    APROBADO = 'aprobado'

    STATUS = (
        (ESPERA, 'En Espera'),
        (RECHAZADO, 'Rechazado'),
        (APROBADO, 'Aprobado')
    )
    usuario = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='actividades')
    clase = models.CharField(choices=CLASES, max_length=30, blank=True, null=True)

    # ubicacion
    sede = models.ForeignKey('ubicacion.Sede', blank=True, null=True, related_name='actividades',
                             on_delete=models.SET_NULL)
    unidad = models.ForeignKey('ubicacion.UnidadInstancia', blank=True, null=True, related_name='actividades',
                               on_delete=models.SET_NULL)
    ubicacion = models.ForeignKey('ubicacion.SeccionInstancia', blank=True, null=True, related_name='actividades',
                                  on_delete=models.SET_NULL)
    cod_sede = models.CharField(max_length=2, blank=True)
    cod_unidad = models.CharField(max_length=2, blank=True)
    cod_seccion = models.CharField(max_length=2, blank=True)

    fecha = models.DateField()  # Fecha en que se dio la actividad
    fecha_creacion = models.DateTimeField(blank=True)  # Fecha en que se registro la actividad
    nombre_actividad = models.CharField(max_length=120)
    resumen = models.TextField(max_length=1000, blank=True)
    estado = models.CharField(max_length=25, choices=STATUS, default='espera')
    motivo_rechazo = models.TextField(max_length=500, blank=True)

    objects = ActividadManager()

    class Meta:
        permissions = (
            ('aprobar_actividad', 'Aprobar Actividad'),
        )
        verbose_name_plural = 'Actividades'
        unique_together = ('usuario', 'nombre_actividad')

    def __str__(self):
        return '{}: {}'.format(self.fecha, self.clase)

    def save(self, *args, **kwargs):
        try:
            p = Perfil.objects.get(usuario=self.usuario)
            if p:
                try:
                    self.cod_sede = p.cod_sede
                    self.cod_unidad = p.cod_unidad
                    self.cod_seccion = p.cod_seccion
                    self.ubicacion = SeccionInstancia.objects.get(cod_sede=self.cod_sede, cod_unidad=self.cod_unidad,
                                                                  cod_seccion=self.cod_seccion)
                except:
                    logger.error(
                        'Hubo un error al asignar ubicacion {}-{}-{} a la actividad'.format(self.cod_sede,
                                                                                            self.cod_unidad,
                                                                                            self.cod_seccion))
        except:
            logger.error('Error! No se pudo encontrar un usuario durante la creacion de la actividad.')
        self.fecha_creacion = timezone.now()
        return super(Actividad, self).save()

    def aprobar(self):
        self.estado = 'aprobado'
        self.save()

    def rechazar(self):
        self.estado = 'rechazado'
        self.save()

    def espera(self):
        self.estado = 'espera'
        self.save()


class EstadiaPostdoctoral(Actividad):
    lugar = models.CharField(max_length=1020)
    archivo = models.FileField(blank=True, upload_to='files/estadias-postdoctorales')

    class Meta:
        verbose_name_plural = 'Estadias postdoctorales'

    def __str__(self):
        return '{}'.format(self.fecha)

    def save(self, *args, **kwargs):
        self.clase = self.ESTADIA
        return super(EstadiaPostdoctoral, self).save()


class Publicacion(Actividad):
    REVISTA_ESPECIALIZADA = 'revista_especializada_internacional'
    REVISTA_GENERAL_I = 'revista_general_internacional'
    REVISTA_GENERAL_N = 'revista_general_nacional'
    PERIODICO_N = 'periodico_nacional'
    PERIODICO_I = 'periodicio_ilimitado'
    BOLETIN = 'boletin'
    GACETA = 'gaceta'
    OTRO = 'otros'

    TIPOS = (
        (REVISTA_ESPECIALIZADA, 'Revista Especializada Internacional'),
        (REVISTA_GENERAL_I, 'Revista General Internacional'),
        (REVISTA_GENERAL_N, 'Revista General Nacional'),
        (PERIODICO_N, 'Periodico Nacional'),
        (PERIODICO_I, 'Periodico Ilimitado'),
        (BOLETIN, 'Boletin'),
        (GACETA, 'Gaceta'),
        (OTRO, 'Otros'))
    tipo = models.CharField(max_length=100, choices=TIPOS, default='otros')
    lugar_publicacion = models.CharField(max_length=1020)
    archivo = models.FileField(blank=True, upload_to='files/publicaciones')

    class Meta:
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return '{} - {}'.format(self.fecha, self.usuario.get_full_name())

    def save(self, *args, **kwargs):
        self.clase = self.PUBLICACION
        return super(Publicacion, self).save()


class Investigacion(Actividad):
    codigo = models.CharField(max_length=100)
    archivo = models.FileField(blank=True, upload_to='files/investigaciones')

    class Meta:
        unique_together = ('codigo',)
        verbose_name_plural = 'Investigaciones'

    def save(self, *args, **kwargs):
        self.clase = self.INVESTIGACION
        return super(Investigacion, self).save()

    def __str__(self):
        return '{} - {}'.format(self.fecha, self.usuario.get_full_name())


class Libro(Actividad):
    isbn = models.CharField(max_length=1020)
    editorial = models.CharField(max_length=1020)
    archivo = models.FileField(blank=True, upload_to='files/libros')

    class Meta:
        unique_together = ('isbn',)
        verbose_name_plural = 'Libros'

    def __str__(self):
        return '{} - {}'.format(self.fecha, self.usuario.get_full_name())

    def save(self, *args, **kwargs):
        self.clase = self.LIBRO
        return super(Libro, self).save()


class Conferencia(Actividad):
    archivo = models.FileField(blank=True, null=True, upload_to='files/conferencias')

    class Meta:
        verbose_name_plural = 'Conferencia'

    def __str__(self):
        return '{} - {}'.format(self.fecha, self.usuario.get_full_name())

    def save(self, *args, **kwargs):
        self.clase = self.CONFERENCIA
        return super(Conferencia, self).save()


class Ponencia(Actividad):
    pais = CountryField()
    archivo = models.FileField(blank=True, null=True, upload_to='files/ponencias')

    class Meta:
        verbose_name_plural = 'Ponencias'

    def __str__(self):
        return '{} - {}'.format(self.fecha, self.usuario.get_full_name())

    def save(self, *args, **kwargs):
        self.clase = self.PONENCIA
        return super(Ponencia, self).save()


class Proyecto(Actividad):
    ESTUDIO = 'estudio'
    ASESORIA = 'asesoria'
    PLANOS = 'planos'
    ESPECIFICACION = 'especificacion'
    PROYECTO = 'proyecto'
    APLICACION = 'aplicacion'
    POEMARIO = 'poemario'
    LIBRETO = 'libreto'
    RECITAL = 'recital'
    TEATRO = 'teatro'
    ACTUACION = 'actuacion'
    DANZA = 'danza'
    CONCIERTO = 'concierto'
    PRODUCCION = 'produccion'
    AUDIOVISUAL = 'audiovisual'
    GRAFICO = 'grafico'
    ARTE = 'arte'

    TIPOS = (
        (ESTUDIO, 'Estudio de Factibilidad'),
        (ASESORIA, 'Asesoria'),
        (PLANOS, 'Planos'),
        (ESPECIFICACION, 'Especificaciones Tecnicas'),
        (PROYECTO, 'Proyectos'),
        (APLICACION, 'Desarrollo de Aplicaciones'),
        (POEMARIO, 'Poemarios'),
        (LIBRETO, 'Libretos'),
        (RECITAL, 'Recitales'),
        (TEATRO, 'Direccion de Teatro'),
        (ACTUACION, 'Actuacion'),
        (DANZA, 'Danza'),
        (CONCIERTO, 'Conciertos'),
        (PRODUCCION, 'Produccion Artistica'),
        (AUDIOVISUAL, 'Audiovisual'),
        (GRAFICO, 'Diseno Grafico'),
        (ARTE, 'Obra de Arte')
    )
    archivo = models.FileField(blank=True, null=True, upload_to='files/actividad')  # TODO: upload_to? :P
    tipo = models.CharField(max_length=100, choices=TIPOS)

    class Meta:
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return '{} - {}'.format(self.fecha, self.usuario.get_full_name())

    def save(self, *args, **kwargs):
        self.clase = self.PROYECTO
        return super(Proyecto, self).save()


class Premio(Actividad):
    TIPOS = (
        ('nacional', 'Nacional'),
        ('internacional', 'Internacional')
    )
    tipo = models.CharField(max_length=100, choices=TIPOS)
    archivo = models.FileField(upload_to='files/premios', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Premios'

    def __str__(self):
        return '{} - {}'.format(self.fecha, self.usuario.get_full_name())

    def save(self, *args, **kwargs):
        self.clase = self.PREMIO
        return super(Premio, self).save()


class Idioma(Actividad):
    BASICO = 'basico'
    INTERMEDIO = 'intermedio'
    AVANZADO = 'avanzado'
    NATIVO = 'nativo'

    NIVELES = (
        (BASICO, 'Basico'),
        (INTERMEDIO, 'Intermedio'),
        (AVANZADO, 'Avanzado'),
        (NATIVO, 'Nativo'),
    )
    nombre = models.CharField(max_length=7, choices=LANGUAGES)
    nivel_hablado = models.CharField(max_length=15, default=NATIVO, choices=NIVELES)
    nivel_escrito = models.CharField(max_length=15, default=NATIVO, choices=NIVELES)

    class Meta:
        verbose_name_plural = 'Idiomas'

    def __str__(self):
        return self.usuario.get_full_name() + ' - ' + self.get_nombre_display()

    def save(self, *args, **kwargs):
        self.clase = self.IDIOMA
        self.nombre_actividad = 'Idioma - {}'.format(self.nombre)
        self.fecha = timezone.now()
        return super(Idioma, self).save()


class InfoTitulo(models.Model):
    LICENCIATURA = 'licenciatura'
    POSTGRADO = 'postgrado'
    MAESTRIA = 'maestria'
    DOCTORADO = 'doctorado'
    NIVEL = (
        (LICENCIATURA, 'Licenciatura'),
        (POSTGRADO, 'Postgrado'),
        (MAESTRIA, 'Maestria'),
        (DOCTORADO, 'Doctorado')
    )
    nombre = models.CharField(max_length=120, unique=True)
    nivel = models.CharField(max_length=25, choices=NIVEL)

    class Meta:
        verbose_name_plural = 'Informacion de Titulos'

    def __str__(self):
        return self.nombre


class CentroEstudio(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    pais = CountryField()

    class Meta:
        unique_together = ('nombre', 'pais')
        verbose_name_plural = 'Centros de Estudio'

    def __str__(self):
        return self.nombre


class Titulo(Actividad):
    info_titulo = models.ForeignKey(InfoTitulo, on_delete=models.CASCADE)
    centro_estudio = models.ForeignKey(CentroEstudio, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='titulos/', blank=True)

    class Meta:
        verbose_name = 'Titulos'

    def __str__(self):
        profesor = self.usuario.get_full_name()
        nombre_titulo = self.info_titulo.nombre
        centro_estudio = self.centro_estudio.nombre
        return profesor + ' - ' + nombre_titulo + ' - ' + centro_estudio

    def save(self, *args, **kwargs):
        self.clase = self.TITULO
        self.nombre_actividad = " " + self.info_titulo.nombre
        return super(Titulo, self).save()
