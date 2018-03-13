from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.urls import reverse

from django_countries.fields import CountryField

from .managers import EstudianteManager, AnteproyectoManager, ProyectoManager

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
    provincia = models.CharField(
        max_length=5, blank=True, choices=PROVINCIAS, default='00')
    clase = models.CharField(max_length=5, blank=True,
                             choices=CLASE, default='00')
    tomo = models.CharField(max_length=5, blank=True, default='000')
    folio = models.CharField(max_length=5, blank=True, default='0000')
    primer_nombre = models.CharField(max_length=120, blank=True)
    segundo_nombre = models.CharField(max_length=120, blank=True)
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
    cod_sede = models.CharField(max_length=2, blank=True, default='XX')
    cod_facultad = models.CharField(max_length=2, blank=True, default='XX')
    cod_escuela = models.CharField(max_length=2, blank=True, default='XX')
    cod_carrera = models.CharField(max_length=2, blank=True, default='XX')
    turno = models.CharField(max_length=1, blank=True,
                             choices=TURNOS)
    fecha_ingreso = models.DateField(blank=True, null=True)
    semestre_ingreso = models.CharField(
        max_length=1, blank=True, choices=SEMESTRES)
    ultimo_anio = models.CharField(max_length=4, blank=True)
    ultimo_semestre = models.CharField(max_length=1, blank=True)  # I, II, V
    fecha_graduacion = models.DateField(blank=True, null=True)

    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True, related_name='estudiantes',
                             blank=True)
    facultad = models.ForeignKey(UnidadInstancia, on_delete=models.SET_NULL, null=True,
                                 related_name='estudiantes', blank=True)
    escuela = models.ForeignKey(SeccionInstancia, on_delete=models.SET_NULL, null=True,
                                related_name='estudiantes', blank=True)
    carrera = models.ForeignKey(CarreraInstancia, on_delete=models.SET_NULL, null=True,
                                related_name='estudiantes',
                                blank=True)

    objects = EstudianteManager()

    class Meta:
        unique_together = ('provincia', 'clase', 'tomo', 'folio')
        permissions = (
            ('view_estudiante', 'Can view estudiante'),
        )

    def save(self, *args, **kwargs):
        try:
            self.sede = Sede.objects.get(cod_sede=self.cod_sede)
            self.unidad = UnidadInstancia.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad)
            self.escuela = SeccionInstancia.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad,
                                                        cod_escuela=self.cod_escuela)
            self.carrera = CarreraInstancia.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad,
                                                        cod_escuela=self.cod_escuela,
                                                        cod_carrera=self.cod_carrera)
        except:
            print('Hubo un error al guardar los datos del estudiante{}{}{}{}. Error: {}'.format(self.provincia,
                                                                                                self.clase, self.tomo,
                                                                                                self.folio,
                                                                                                1))  # TODO: sys.exc
        return super(Estudiante, self).save()

    def __str__(self):
        return '{}, {}'.format(self.primer_apellido, self.primer_nombre)

    def get_absolute_url(self):
        return reverse('estudiante:detalle', kwargs={'pk': self.pk})


# TODO: Combinar con Trabajo de Graduacion.
class Anteproyecto(models.Model):
    ESTADO = (
        ('pendiente', 'Pendiente'),
        ('rechazado', 'Rechazado'),
        ('aprobado', 'Aprobado')
    )
    # region Ubicacion
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='anteproyectos')
    facultad = models.ForeignKey(UnidadInstancia, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='anteproyectos')
    escuela = models.ForeignKey(SeccionInstancia, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='anteproyectos')
    carrera = models.ForeignKey(CarreraInstancia, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='anteproyectos')
    estudiante = models.ManyToManyField(Estudiante, related_name='anteproyectos')
    cod_sede = models.CharField(max_length=120, blank=True)
    cod_facultad = models.CharField(max_length=120, blank=True)
    cod_escuela = models.CharField(max_length=120, blank=True)
    cod_carrera = models.CharField(max_length=120, blank=True)
    # endregion
    asesor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               related_name='anteproyecto', limit_choices_to=Q(groups__name='Profesores'))
    nombre_proyecto = models.CharField(max_length=120, blank=True)
    registrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='registros')
    fecha_registro = models.DateField(blank=True, null=True, auto_now_add=True)
    fecha_aprobacion = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=15, choices=ESTADO, default='pendiente')
    archivo = models.FileField(blank=True)
    resumen = models.TextField(max_length=500, blank=True)

    objects = AnteproyectoManager()

    class Meta:
        permissions = (
            ('aprobar_anteproyecto', 'Aprobar Anteproyecto'),
            ('ver_anteproyecto_facultad', 'Ver Anteproyectos en Facultad'),
            ('ver_anteproyecto_escuela', 'Ver Anteproyecto en Escuela'),
        )

    def __str__(self):
        return self.nombre_proyecto

    def get_absolute_url(self):
        return reverse('estudiante:anteproyecto-detalle', kwargs={
            'pk': self.pk
        })

    def save(self, *args, **kwargs):
        self.cod_sede = self.registrado_por.perfil.cod_sede
        self.cod_facultad = self.registrado_por.perfil.cod_facultad
        self.cod_escuela = self.registrado_por.perfil.cod_escuela
        self.sede = self.registrado_por.perfil.sede
        self.facultad = self.registrado_por.perfil.facultad
        self.escuela = self.registrado_por.perfil.escuela
        self.carrera = CarreraInstancia.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad,
                                                    cod_escuela=self.cod_escuela, cod_carrera=self.cod_carrera)
        return super(Anteproyecto, self).save()


class Proyecto(models.Model):
    LICENCIATURA = 'licenciatura'
    ESPECIALIZACION = 'especializacion'
    MAESTRIA = 'maestria'
    DOCTORADO = 'doctorado'
    PROGRAMAS = (
        (LICENCIATURA, 'Licenciatura'),
        (ESPECIALIZACION, 'Especialización'),
        (MAESTRIA, 'Maestria'),
        (DOCTORADO, 'Doctorado')
    )
    cod_sede = models.CharField(max_length=120, blank=True)
    cod_facultad = models.CharField(max_length=120, blank=True)
    cod_escuela = models.CharField(max_length=120, blank=True)
    cod_carrera = models.CharField(max_length=120, blank=True)
    facultad = models.ForeignKey(UnidadInstancia, on_delete=models.SET_NULL, null=True,
                                 related_name='proyectos')
    escuela = models.ForeignKey(SeccionInstancia, on_delete=models.SET_NULL, null=True,
                                related_name='proyectos')
    carrera = models.ForeignKey(CarreraInstancia, on_delete=models.SET_NULL, null=True,
                                related_name='proyectos')
    estudiante = models.ManyToManyField(Estudiante, related_name='proyectos')
    anteproyecto = models.ForeignKey(
        Anteproyecto, on_delete=models.SET_NULL, null=True)
    jurados = models.ManyToManyField(User, related_name='jurado', limit_choices_to={
        'groups__name': 'Profesores'
    })
    fecha_entrega = models.DateField(blank=True, null=True)
    fecha_sustentacion = models.DateField(blank=True, null=True)
    programa = models.CharField(max_length=25, choices=PROGRAMAS, default=LICENCIATURA)
    nota = models.CharField(max_length=3, blank=True)
    detalle = models.TextField(max_length=500, blank=True)
    archivo = models.FileField(blank=True)

    objects = ProyectoManager

    class Meta:
        permissions = (
            ('ver_proyecto_facultad', 'Ver proyectos en facultad'),
            ('ver_proyecto_escuela', 'Ver proyectos en escuela')
        )

    def __str__(self):
        return 'Proyecto {}'.format(self.anteproyecto.nombre_proyecto)

    def get_absolute_url(self):
        return reverse('estudiante:proyecto', kwargs={'pk': self.pk})


def regions_changed(sender, **kwargs):
    if kwargs['instance'].jurados.count() > 3:
        raise ValidationError("No puede asignar mas de 3 jurados.")


m2m_changed.connect(regions_changed, sender=Proyecto.jurados.through)
