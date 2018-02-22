from django.apps import apps
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.urls import reverse

from django_countries.fields import CountryField

from .managers import EstudianteManager, AnteproyectoManager

from ubicacion.models import Sede, UnidadInstancia, SeccionInstancia, CarreraInstancia


class Estudiante(models.Model):
    SEXO = (
        ('M', 'Hombre'),
        ('F', 'Mujer')
    )
    SEMESTRES = (
        ('0', ''),
        ('1', 'I'),
        ('2', 'II')
    )
    TURNOS = (
        ('D', 'Diurno'),
        ('V', 'Vespertino'),
        ('N', 'Nocturno')
    )
    PROVINCIAS = (
        ('0', '00'),
        ('1', '01'),
        ('2', '02'),
        ('3', '03'),
        ('4', '04'),
        ('5', '05'),
        ('6', '06'),
        ('7', '07'),
        ('8', '08'),
        ('9', '09'),
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
    SANGRE = (
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-')
    )
    # Informacion cedula del estudiante
    provincia = models.CharField(
        max_length=5, blank=True, choices=PROVINCIAS, default='00')
    clase = models.CharField(max_length=5, blank=True,
                             choices=CLASE, default='00')
    tomo = models.CharField(max_length=5, blank=True, default='000')
    folio = models.CharField(max_length=5, blank=True, default='0000')

    # Información personal del estudiante
    # Actualmente en el sistema se registra como los dos
    primer_nombre = models.CharField(max_length=120, blank=True)
    segundo_nombre = models.CharField(max_length=120, blank=True)
    # Actualmente en el sistema se registra como los dos
    primer_apellido = models.CharField(max_length=120, blank=True)
    segundo_apellido = models.CharField(max_length=120, blank=True)

    direccion = models.CharField(max_length=120, blank=True)
    sexo = models.CharField(max_length=120, blank=True, choices=SEXO)
    telefono = models.CharField(max_length=120, blank=True)
    tipo_sangre = models.CharField(max_length=120, blank=True, choices=SANGRE)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    discapacidad = models.TextField(max_length=500, blank=True)

    # Informacion de contacto
    pais = CountryField(blank=True)
    correo = models.EmailField(blank=True)
    telefono_oficina = models.CharField(max_length=10, blank=True)
    celular = models.CharField(max_length=12, blank=True)
    celular_oficina = models.CharField(max_length=12, blank=True)  #

    # Informacion academica
    cod_sede = models.CharField(max_length=2, blank=True, default='XX')
    cod_unidad = models.CharField(max_length=2, blank=True, default='XX')
    cod_seccion = models.CharField(max_length=2, blank=True, default='XX')
    cod_carrera = models.CharField(max_length=2, blank=True, default='XX')
    turno = models.CharField(max_length=1, blank=True,
                             choices=TURNOS)  # una letra, d, v, n
    # Actualmente se registra es el anio de ingreso (como int)
    fecha_ingreso = models.DateField(blank=True, null=True)
    semestre_ingreso = models.CharField(
        max_length=1, blank=True, choices=SEMESTRES)
    # Se refiere a ultimo anio de matricula.
    ultimo_anio = models.CharField(max_length=4, blank=True)
    ultimo_semestre = models.CharField(max_length=1, blank=True)  # I, II, V
    fecha_graduacion = models.DateField(blank=True, null=True)
    # ano_cursa = models.CharField(max_length=1, blank=True)  # romanos

    # Información Academica
    sede = models.ForeignKey('ubicacion.Sede', on_delete=models.SET_NULL, null=True, related_name='estudiantes',
                             blank=True)
    unidad = models.ForeignKey('ubicacion.UnidadInstancia', on_delete=models.SET_NULL, null=True,
                               related_name='estudiantes', blank=True)
    escuela = models.ForeignKey('ubicacion.SeccionInstancia', on_delete=models.SET_NULL, null=True,
                                related_name='estudiantes', blank=True)
    carrera = models.ForeignKey('ubicacion.CarreraInstancia', on_delete=models.SET_NULL, null=True,
                                related_name='estudiantes',
                                blank=True)

    objects = EstudianteManager()

    class Meta:
        unique_together = ('provincia', 'clase', 'tomo', 'folio')
        permissions = (
            ('view_estudiante', 'Can view estudiante'),
        )

    def save(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        try:
            sede = apps.get_model('ubicacion', 'Sede')
            facultad = apps.get_model('ubicacion', 'UnidadInstancia')
            escuela = apps.get_model('ubicacion', 'SeccionInstancia')
            carrera = apps.get_model('ubicacion', 'CarreraInstancia')
            self.sede = sede.objects.get(cod_sede=self.cod_sede)
            self.unidad = facultad.objects.get(cod_sede=self.cod_sede, cod_unidad=self.cod_unidad)
            self.escuela = escuela.objects.get(cod_sede=self.cod_sede, cod_unidad=self.cod_unidad,
                                               cod_seccion=self.cod_seccion)
            self.carrera = carrera.objects.get(cod_sede=self.cod_sede, cod_unidad=self.cod_unidad,
                                               cod_seccion=self.cod_seccion,
                                               cod_carrera=self.cod_carrera)
        except:
            pass
        return super(Estudiante, self).save()

    def __str__(self):
        return '{}, {}'.format(self.primer_apellido, self.primer_nombre)

    def get_absolute_url(self):
        return reverse('estudiante:detalle', kwargs={'pk': self.pk})

    def anteproyectos_aprobados(self):
        # TODO: Pasar esto al manager de anteproyectos
        return self.anteproyectos.filter(estado='aprobado')


class Anteproyecto(models.Model):
    """

    """
    ESTADO = (
        ('pendiente', 'Pendiente'),
        ('rechazado', 'Rechazado'),
        ('aprobado', 'Aprobado')
    )
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='anteproyectos')
    unidad = models.ForeignKey(UnidadInstancia, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='anteproyectos')
    seccion = models.ForeignKey(SeccionInstancia, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='anteproyectos')
    carrera = models.ForeignKey(CarreraInstancia, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='anteproyectos')
    estudiante = models.ManyToManyField(Estudiante, related_name='anteproyectos')
    cod_sede = models.CharField(max_length=120, blank=True)
    cod_unidad = models.CharField(max_length=120, blank=True)
    cod_seccion = models.CharField(max_length=120, blank=True)
    cod_carrera = models.CharField(max_length=120, blank=True)
    asesor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               related_name='anteproyecto', limit_choices_to=Q(groups__name='Profesores'))
    nombre_proyecto = models.CharField(max_length=120, blank=True)

    fecha_registro = models.DateField(blank=True, null=True)
    fecha_aprobacion = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=15, choices=ESTADO, default='pendiente')
    archivo = models.FileField(blank=True)
    resumen = models.TextField(max_length=500, blank=True)

    objects = AnteproyectoManager()

    class Meta:
        permissions = (
            ('aprobar_anteproyecto', 'Aprobar Anteproyecto'),
        )

    def __str__(self):
        return self.nombre_proyecto

    def get_absolute_url(self):
        return reverse('estudiante:anteproyecto-detalle', kwargs={
            'pk': self.pk
        })

    def save(self, *args, **kwargs):
        # self.cod_sede = self.carrera.cod_sede
        # self.cod_unidad = self.carrera.cod_unidad
        # self.cod_seccion = self.carrera.cod_seccion
        # self.cod_carrera = self.carrera.cod_carrera
        # try:
        #     sede = apps.get_model('ubicacion', 'Sede')
        #     facultad = apps.get_model('ubicacion', 'UnidadInstancia')
        #     escuela = apps.get_model('ubicacion', 'SeccionInstancia')
        #     carrera = apps.get_model('ubicacion', 'CarreraInstancia')
        #     self.sede = sede.objects.get(cod_sede=self.cod_sede)
        #     self.unidad = facultad.objects.get(cod_sede=self.cod_sede, cod_unidad=self.cod_unidad)
        #     self.escuela = escuela.objects.get(cod_sede=self.cod_sede, cod_unidad=self.cod_unidad,
        #                                        cod_seccion=self.cod_seccion)
        #     self.carrera = carrera.objects.get(cod_sede=self.cod_sede, cod_unidad=self.cod_unidad,
        #                                        cod_seccion=self.cod_seccion,
        #                                        cod_carrera=self.cod_carrera)
        # except:
        #     pass
        self.sede = self.estudiante[0].sede
        self.unidad = self.estudiante[0].unidad
        self.seccion = self.estudiante[0].escuela
        self.carrera = self.estudiante[0].carrera
        return super(Anteproyecto, self).save()


class Proyecto(models.Model):
    PROGRAMAS = (
        ('1', 'Licenciatura'),
        ('2', 'Especialización'),
        ('3', 'Maestria'),
        ('4', 'Doctorado')
    )
    unidad = models.ForeignKey('ubicacion.UnidadInstancia', on_delete=models.SET_NULL, null=True,
                                related_name='proyectos')
    seccion = models.ForeignKey('ubicacion.SeccionInstancia', on_delete=models.SET_NULL, null=True,
                                related_name='proyectos')
    carrera = models.ForeignKey('ubicacion.CarreraInstancia', on_delete=models.SET_NULL, null=True,
                                related_name='proyectos')
    estudiante = models.ManyToManyField(Estudiante, related_name='proyectos')
    anteproyecto = models.ForeignKey(
        Anteproyecto, on_delete=models.SET_NULL, null=True)
    jurados = models.ManyToManyField(User, related_name='jurado', limit_choices_to=Q(
        groups__name='Profesores'))  # Extender para que se pueda consultar desde
    fecha_entrega = models.DateField(blank=True, null=True)
    fecha_sustentacion = models.DateField(blank=True, null=True)
    programa = models.CharField(max_length=1, choices=PROGRAMAS, default='1')
    nota = models.CharField(max_length=3, blank=True)
    detalle = models.TextField(max_length=500, blank=True)
    archivo = models.FileField(blank=True)

    def __str__(self):
        return self.anteproyecto.nombre_proyecto

    def clean(self):
        if self.jurados.count() > 3:
            raise ValidationError('No se puede asignar mas de 3 jurados.')
        super(Proyecto, self).clean()

    def get_absolute_url(self):
        return reverse('estudiante:proyecto', kwargs={'pk': self.pk})
