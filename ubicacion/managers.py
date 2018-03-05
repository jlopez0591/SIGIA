from django.db import models
from django.contrib.auth.models import User

class SedeQuerySet(models.QuerySet):
    def activas(self):
        return self.filter(activo=True)

    def inactivas(self):
        return self.filter(activo=False)

    def campus(self):
        return self.filter(tipo='1')

    def centros(self):
        return self.filter(tipo='2')

    def extensiones(self):
        return self.filter(tipo='3')

    def proyectos(self):
        return self.filter(tipo='4')

    def profesores(self):
        return User.objects.get(perfil__cod_sede=self.cod_sede)


class SedeManager(models.Manager):
    def get_by_natural_key(self, codigo):
        return self.get(cod_sede=codigo)

    def get_queryset(self):
        return SedeQuerySet(self.model, using=self._db)

    def activas(self):
        return self.get_queryset().activas()

    def inactivas(self):
        return self.get_queryset().inactivas()

    def campus(self):
        return self.get_queryset().campus()

    def centros(self):
        return self.get_queryset().centros()

    def extensiones(self):
        return self.get_queryset().extensiones()

    def proyectos(self):
        return self.get_queryset().proyectos()

    def profesores(self):
        return self.get_queryset().profesores()


class UnidadQuerySet(models.QuerySet):
    def activas(self):
        return self.filter(activo=True)

    def inactivas(self):
        return self.filter(activo=False)

    def facultades(self):
        return self.filter(tipo='1')

    def vicerrectorias(self):
        return self.filter(tipo='2')

    def institutos(self):
        return self.filter(tipo='3')

    def finanzas(self):
        return self.filter(tipo='4')

    def asociaciones(self):
        return self.filter(tipo='5')

    def coordinaciones(self):
        return self.filter(tipo='6')


class UnidadManager(models.Manager):
    def get_by_natural_key(self, codigo):
        return self.get(cod_facultad=codigo)

    def get_queryset(self):
        return UnidadQuerySet(self.model, using=self._db)

    def activas(self):
        return self.get_queryset().activas()

    def inactivas(self):
        return self.get_queryset().inactivas()

    def facultades(self):
        return self.get_queryset().facultades()

    def vicerrectorias(self):
        return self.get_queryset().vicerrectorias()

    def finanzas(self):
        return self.get_queryset().finanzas()

    def asociaciones(self):
        return self.get_queryset().asociaciones()

    def coordinaciones(self):
        return self.get_queryset().coordinaciones()


class SeccionQuerySet(models.QuerySet):
    def escuelas(self):
        return self.filter(tipo='ES')

    def departamentos(self):
        return self.filter(tipo='DE')

    def coordinaciones(self):
        return self.filter(tipo='3')

    def decanatos(self):
        return self.filter(tipo='4')

    def oficinas(self):
        return self.filter(tipo='5')

    def organizaciones(self):
        return self.filter(tipo='6')

    def activas(self):
        return self.filter(activo=True)

    def inactivas(self):
        return self.filter(activo=False)


class SeccionManager(models.Manager):
    def get_by_natural_key(self, cod_facultad, cod_escuela):
        return self.get(cod_facultad=cod_facultad, cod_escuela=cod_escuela)

    def get_queryset(self):
        return SeccionQuerySet(self.model, using=self._db)

    def escuelas(self):
        return self.get_queryset().escuelas()

    def deparamentos(self):
        return self.get_queryset().departamentos()

    def coordinaciones(self):
        return self.get_queryset().coordinaciones()

    def decanatos(self):
        return self.get_queryset().decanatos()

    def oficinas(self):
        return self.get_queryset().oficinas()

    def organizaciones(self):
        return self.get_queryset().organizaciones()

    def activas(self):
        return self.get_queryset().activas()

    def inactivas(self):
        return self.get_queryset().inactivas()


class CarreraQuerySet(models.QuerySet):
    def regulares(self):
        return self.filter(tipo='1')

    def postgrados(self):
        return self.filter(tipo='2')

    def maestrias(self):
        return self.filter(tipo='3')

    def doctorados(self):
        return self.filter(tipo='4')

    def cursos(self):
        return self.filter(tipo='5')

    def activas(self):
        return self.filter(activo=True)

    def inactivas(self):
        return self.filter(activo=False)


class CarreraManager(models.Manager):
    def get_by_natural_key(self, cod_facultad, cod_escuela, cod_carrera):
        return self.get(cod_facultad=cod_facultad, cod_escuela=cod_escuela, cod_carrera=cod_carrera)

    def get_queryset(self):
        return CarreraQuerySet(self.model, using=self._db)

    def regulares(self):
        return self.get_queryset().regulares()

    def postgrados(self):
        return self.get_queryset().postgrados()

    def maestrias(self):
        return self.get_queryset().maestrias()

    def doctorados(self):
        return self.get_queryset().doctorados()

    def cursos(self):
        return self.get_queryset().cursos()

    def activas(self):
        return self.get_queryset().activas()

    def inactivas(self):
        return self.get_queryset().inactivas()


class UnidadInstanciasQuerySet(models.QuerySet):
    def activas(self):
        return self.filter(activo=True)

    def inactivas(self):
        return self.filter(activo=False)

    def facultades(self):
        return self.filter(unidad__tipo='1')

    def vicerrectorias(self):
        return self.filter(unidad__tipo='2')

    def institutos(self):
        return self.filter(unidad__tipo='3')

    def finanzas(self):
        return self.filter(unidad__tipo='4')

    def asociaciones(self):
        return self.filter(unidad__tipo='5')

    def coordinaciones(self):
        return self.filter(unidad__tipo='6')


class UnidadInstanciaManager(models.Manager):
    def get_by_natural_key(self, cod_sede, cod_facultad):
        return self.get(cod_sede=cod_sede, cod_facultad=cod_facultad)

    def get_queryset(self):
        return UnidadInstanciasQuerySet(self.model, using=self._db)

    def activas(self):
        return self.get_queryset().activas()

    def inactivas(self):
        return self.get_queryset().inactivas()

    def facultades(self):
        return self.get_queryset().facultades()

    def vicerrectorias(self):
        return self.get_queryset().vicerrectorias()

    def institutos(self):
        return self.get_queryset().institutos()

    def finanzas(self):
        return self.get_queryset().finanzas()

    def asociaciones(self):
        return self.get_queryset().asociaciones()

    def coordinaciones(self):
        return self.get_queryset().coordinaciones()


class SeccionInstanciaQuerySet(models.QuerySet):
    def activas(self):
        return self.filter(activo=True)

    def inactivas(self):
        return self.filter(activo=False)

    def escuelas(self):
        return self.filter(seccion__tipo='ES')

    def departamentos(self):
        return self.filter(seccion__tipo='DE')

    def coordinaciones(self):
        return self.filter(seccion__tipo='3')

    def decanato(self):
        return self.filter(seccion__tipo='4')

    def oficinas(self):
        return self.filter(seccion__tipo='5')

    def organizaciones(self):
        return self.filter(seccion__tipo='6')


class SeccionInstanciaManager(models.Manager):
    def get_by_natural_key(self, cod_sede, cod_facultad, cod_escuela):
        return self.get(cod_sede=cod_sede, cod_facultad=cod_facultad, cod_escuela=cod_escuela)

    def get_queryset(self):
        return SeccionInstanciaQuerySet(self.model, using=self._db)

    def activas(self):
        return self.get_queryset().activas()

    def inactivas(self):
        return self.get_queryset().inactivas()

    def escuelas(self):
        return self.get_queryset().escuelas()

    def departamentos(self):
        return self.get_queryset().departamentos()

    def coordinaciones(self):
        return self.get_queryset().coordinaciones()

    def decanato(self):
        return self.get_queryset().decanato()

    def oficinas(self):
        return self.get_queryset().oficinas()

    def organizaciones(self):
        return self.get_queryset().organizaciones()


class CarreraInstanciaQuerySet(models.QuerySet):
    def activas(self):
        return self.filter(activo=True)

    def inactivas(self):
        return self.filter(activo=False)

    def regulares(self):
        return self.filter(carrera__tipo='1')

    def postgrados(self):
        return self.filter(carrera__tipo='2')

    def maestrias(self):
        return self.filter(carrera__tipo='3')

    def doctorados(self):
        return self.filter(carrera__tipo='4')

    def cursos(self):
        return self.filter(carrera__tipo='5')


class CarreraInstanciaManager(models.Manager):
    def get_by_natural_key(self, cod_sede, cod_facultad, cod_escuela, cod_carrera):
        return self.get(cod_sede=cod_sede, cod_facultad=cod_facultad, cod_escuela=cod_escuela, cod_carrera=cod_carrera)

    def get_queryset(self):
        return CarreraInstanciaQuerySet(self.model, using=self._db)

    def activas(self):
        return self.get_queryset().activas()

    def inactivas(self):
        return self.get_queryset().inactivas()

    def regulares(self):
        return self.get_queryset().regulares()

    def postgrados(self):
        return self.get_queryset().postgrados()

    def maestrias(self):
        return self.get_queryset().maestrias()

    def doctorados(self):
        return self.get_queryset().doctorados()

    def cursos(self):
        return self.get_queryset().cursos()
