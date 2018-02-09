import datetime
import logging

from django.conf.global_settings import LANGUAGES
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse, reverse_lazy

# Third party imports
from django_countries.fields import CountryField
from polymorphic.models import PolymorphicModel

# Utilities and helpers
from .managers import ActividadManager
from .validators import validate_file_type

# Other apps import
from ubicacion.models import SeccionInstancia, Sede, UnidadInstancia
from perfiles.models import Perfil

logger = logging.getLogger(__name__)


def user_directory_path(instance, filename):
    """
    Retorna el path en el cual salvar los archivos (actividades en este modulo)
    :param instance:
    :param filename:
    :return:
    """
    # actividades/tipo/fecha/usuario/filename
    data = datetime.datetime.now().strftime('%Y/%b')
    return 'actividades/{0}/{1}/{2}/{3}'.format(instance.clase, data, instance.usuario.username, filename)


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
        (ESTADIA, 'Estadia Postdoctoral'),  # Fecha Final
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

    sede = models.ForeignKey('ubicacion.Sede', blank=True, null=True, related_name='actividades',
                             on_delete=models.SET_NULL)
    unidad = models.ForeignKey('ubicacion.UnidadInstancia', blank=True, null=True, related_name='actividades',
                               on_delete=models.SET_NULL)
    departamento = models.ForeignKey('ubicacion.SeccionInstancia', blank=True, null=True, related_name='actividades',
                                     on_delete=models.SET_NULL)
    cod_sede = models.CharField(max_length=2, blank=True)
    cod_unidad = models.CharField(max_length=2, blank=True)
    cod_seccion = models.CharField(max_length=2, blank=True)

    fecha = models.DateField()

    fecha_creacion = models.DateTimeField(blank=True)
    nombre_actividad = models.CharField(max_length=120)
    resumen = models.TextField(max_length=1000, blank=True)
    estado = models.CharField(max_length=25, choices=STATUS, default='espera')
    motivo_rechazo = models.TextField(max_length=500, blank=True)

    archivo = models.FileField(upload_to=user_directory_path, validators=[validate_file_type])

    objects = ActividadManager()

    class Meta:
        permissions = (
            ('aprobar_actividad', 'Aprobar Actividad'),
        )
        verbose_name_plural = 'Actividades'
        unique_together = ('usuario', 'nombre_actividad')

    def __str__(self):
        return '{}: {}'.format(self.fecha, self.clase.capitalize())

    def save(self, *args, **kwargs):
        try:
            p = Perfil.objects.get(usuario=self.usuario)
            if p:
                try:
                    self.sede = p.sede
                    self.unidad = p.unidad
                    self.departamento = p.departamento
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

    def get_edit_url(self):
        opciones = dict()
        opciones[self.ESTADIA] = reverse_lazy('actividad:actualizar-estadia', kwargs={'pk': self.pk})
        opciones[self.PUBLICACION] = reverse_lazy('actividad:actualizar-publicacion', kwargs={'pk': self.pk})
        opciones[self.INVESTIGACION] = reverse_lazy('actividad:actualizar-investigacion', kwargs={'pk': self.pk})
        opciones[self.LIBRO] = reverse_lazy('actividad:actualizar-libro', kwargs={'pk': self.pk})
        opciones[self.CONFERENCIA] = reverse_lazy('actividad:actualizar-conferencia', kwargs={'pk': self.pk})
        opciones[self.PONENCIA] = reverse_lazy('actividad:actualizar-ponencia', kwargs={'pk': self.pk})
        opciones[self.PROYECTO] = reverse_lazy('actividad:actualizar-proyecto', kwargs={'pk': self.pk})
        opciones[self.PREMIO] = reverse_lazy('actividad:actualizar-premio', kwargs={'pk': self.pk})
        opciones[self.IDIOMA] = reverse_lazy('actividad:actualizar-idioma', kwargs={'pk': self.pk})
        opciones[self.TITULO] = reverse_lazy('actividad:actualizar-titulo', kwargs={'pk': self.pk})
        return opciones[self.clase]

    def get_absolute_url(self):
        opciones = dict()
        opciones[self.ESTADIA] = reverse_lazy('actividad:detalle-estadia', kwargs={'pk': self.pk})
        opciones[self.PUBLICACION] = reverse_lazy('actividad:detalle-publicacion', kwargs={'pk': self.pk})
        opciones[self.INVESTIGACION] = reverse_lazy('actividad:detalle-investigacion', kwargs={'pk': self.pk})
        opciones[self.LIBRO] = reverse_lazy('actividad:detalle-libro', kwargs={'pk': self.pk})
        opciones[self.CONFERENCIA] = reverse_lazy('actividad:detalle-conferencia', kwargs={'pk': self.pk})
        opciones[self.PONENCIA] = reverse_lazy('actividad:detalle-ponencia', kwargs={'pk': self.pk})
        opciones[self.PROYECTO] = reverse_lazy('actividad:detalle-proyecto', kwargs={'pk': self.pk})
        opciones[self.PREMIO] = reverse_lazy('actividad:detalle-premio', kwargs={'pk': self.pk})
        opciones[self.IDIOMA] = reverse_lazy('actividad:detalle-idioma', kwargs={'pk': self.pk})
        opciones[self.TITULO] = reverse_lazy('actividad:detalle-titulo', kwargs={'pk': self.pk})
        return opciones[self.clase]


class EstadiaPostdoctoral(Actividad):
    lugar = models.CharField(max_length=1020)
    duracion = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        verbose_name_plural = 'Estadias postdoctorales'

    def __str__(self):
        return '{}'.format(self.fecha)

    def get_absolute_url(self):
        pass

    def get_edit_url(self):
        return reverse('actividad:actualizar-estadia', kwargs={'pk': self.pk})

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

    class Meta:
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return '{} - {}'.format(self.fecha, self.usuario.get_full_name())

    def save(self, *args, **kwargs):
        self.clase = self.PUBLICACION
        return super(Publicacion, self).save()


class Investigacion(Actividad):
    codigo = models.CharField(max_length=100)
    duracion = models.PositiveIntegerField(blank=True, default=0)

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

    class Meta:
        unique_together = ('isbn',)
        verbose_name_plural = 'Libros'

    def __str__(self):
        return '{} - {}'.format(self.fecha, self.usuario.get_full_name())

    def save(self, *args, **kwargs):
        self.clase = self.LIBRO
        return super(Libro, self).save()


class Conferencia(Actividad):
    duracion = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        verbose_name_plural = 'Conferencia'

    def __str__(self):
        return '{} - {}'.format(self.fecha, self.usuario.get_full_name())

    def save(self, *args, **kwargs):
        self.clase = self.CONFERENCIA
        return super(Conferencia, self).save()


class Ponencia(Actividad):
    pais = CountryField()

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
        self.nombre_actividad = 'Idioma - {}'.format(self.get_nombre_display())
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
