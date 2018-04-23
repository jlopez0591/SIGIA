from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField
from .managers import EstudianteManager, TrabajoManager
from ubicacion.models import Sede, FacultadInstancia, EscuelaInstancia, CarreraInstancia

from utils.uploads import trabajo_upload_rename
from utils.validators import validate_file_type


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
    provincia = models.CharField(max_length=5, blank=True, choices=PROVINCIAS, default='00')
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
    discapacidad = models.TextField(max_length=500, blank=True, null=True)
    pais = CountryField(blank=True)
    correo = models.EmailField(blank=True)
    telefono_oficina = models.CharField(max_length=120, blank=True)
    celular = models.CharField(max_length=120, blank=True)
    celular_oficina = models.CharField(max_length=120, blank=True)  #
    cod_sede = models.CharField(max_length=2, blank=True, default='XX')
    cod_facultad = models.CharField(max_length=2, blank=True, default='XX')
    cod_escuela = models.CharField(max_length=2, blank=True, default='XX')
    cod_carrera = models.CharField(max_length=2, blank=True, default='XX')
    turno = models.CharField(max_length=1, blank=True,
                             choices=TURNOS)
    fecha_ingreso = models.DateField(blank=True, null=True)
    semestre_ingreso = models.CharField(
        max_length=5, blank=True, choices=SEMESTRES)
    ultimo_anio = models.CharField(max_length=4, blank=True)
    ultimo_semestre = models.CharField(max_length=5, blank=True)
    fecha_graduacion = models.DateField(blank=True, null=True)

    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True, related_name='estudiantes',
                             blank=True)
    facultad = models.ForeignKey(FacultadInstancia, on_delete=models.SET_NULL, null=True,
                                 related_name='estudiantes', blank=True)
    escuela = models.ForeignKey(EscuelaInstancia, on_delete=models.SET_NULL, null=True,
                                related_name='estudiantes', blank=True)
    carrera = models.ForeignKey(CarreraInstancia, on_delete=models.SET_NULL, null=True,
                                related_name='estudiantes',
                                blank=True)

    history = AuditlogHistoryField()
    objects = EstudianteManager()

    class Meta:
        unique_together = ('provincia', 'clase', 'tomo', 'folio')
        permissions = (
            ('view_estudiante', 'Can view estudiante'),
        )

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
            self.carrera = CarreraInstancia.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad,
                                                        cod_escuela=self.cod_escuela,
                                                        cod_carrera=self.cod_carrera)
        except ObjectDoesNotExist:
            pass
        return super(Estudiante, self).save()

    def __str__(self):
        return '{}, {}'.format(self.primer_apellido, self.primer_nombre)

    def get_absolute_url(self):
        return reverse('estudiante:detalle', kwargs={'pk': self.pk})


class TrabajoGraduacion(models.Model):
    ESTADO = (
        ('pendiente', 'Pendiente'),
        ('rechazado', 'Rechazado'),
        ('aprobado', 'Aprobado'),
        ('sustentado', 'Sustentado')
    )
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
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='trabajos_graduacion')
    facultad = models.ForeignKey(FacultadInstancia, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='trabajos_graduacion')
    escuela = models.ForeignKey(EscuelaInstancia, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='trabajos_graduacion')
    carrera = models.ForeignKey(CarreraInstancia, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='trabajos_graduacion')
    nombre_proyecto = models.CharField(max_length=120, blank=True)
    estudiantes = models.ManyToManyField(Estudiante, related_name='proyectos', blank=True)
    asesor = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='asesorias',
                               limit_choices_to={
                                   'groups__name': 'Profesores'
                               })
    estado = models.CharField(max_length=15, choices=ESTADO, default='pendiente')
    programa = models.CharField(max_length=25, choices=PROGRAMAS, default=LICENCIATURA)

    registrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='registros')

    jurados = models.ManyToManyField(User, related_name='jurado', blank=True, limit_choices_to={
        'groups__name': 'Profesores'
    })

    fecha_entrega = models.DateField(blank=True, null=True)
    fecha_sustentacion = models.DateField(blank=True, null=True)
    nota = models.CharField(max_length=3, blank=True)
    archivo_anteproyecto = models.FileField(blank=True, upload_to=trabajo_upload_rename,
                                            validators=[validate_file_type])
    archivo_trabajo = models.FileField(blank=True, upload_to=trabajo_upload_rename,
                                       validators=[validate_file_type])

    objects = TrabajoManager()

    def __str__(self):
        return self.nombre_proyecto

    class Meta:
        permissions = (
            ('aprobar_trabajo', 'Aprobar Trabajo'),
        )

    def save(self, *args, **kwargs):
        self.cod_sede = self.registrado_por.perfil.cod_sede
        self.cod_facultad = self.registrado_por.perfil.cod_facultad
        self.cod_escuela = self.registrado_por.perfil.cod_escuela
        self.sede = self.registrado_por.perfil.sede
        self.facultad = self.registrado_por.perfil.facultad
        self.escuela = self.registrado_por.perfil.escuela
        try:
            self.carrera = CarreraInstancia.objects.get(cod_sede=self.cod_sede, cod_facultad=self.cod_facultad,
                                                    cod_escuela=self.cod_escuela, cod_carrera=self.cod_carrera)
        except ObjectDoesNotExist:
            pass
        return super(TrabajoGraduacion, self).save()

    def get_absolute_url(self):
        return reverse('estudiante:detalle-trabajo', kwargs={
            'pk': self.pk
        })


auditlog.register(Estudiante)
auditlog.register(TrabajoGraduacion)
