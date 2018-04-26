from datetime import datetime

from django.db import models


class EstudianteQuerySet(models.QuerySet):
    def activos(self):
        return self.filter(ultimo_anio=datetime.now().year)

    def hombres(self):
        return self.filter(ultimo_anio=datetime.now().year)

    def mujeres(self):
        return self.filter(ultimo_anio=datetime.now().year)

    def facultad(self, facultad):
        return self.filter(facultad_id=facultad)

    def escuela(self, escuela):
        return self.filter(escuela_id=escuela)

    def carrera(self, carrera):
        return self.filter(carrera_id=carrera)


class EstudianteManager(models.Manager):
    def get_queryset(self):
        return EstudianteQuerySet(self.model, using=self._db)

    def activos(self):
        return self.get_queryset().activos()

    def hombres(self):
        return self.get_queryset().hombres()

    def mujeres(self):
        return self.get_queryset().mujeres()

    def facultad(self, facultad):
        return self.get_queryset().facultad(facultad)

    def escuela(self, escuela):
        return self.get_queryset().escuela(escuela)

    def carrera(self, carrera):
        return self.get_queryset().carrera(carrera)


class TrabajoQuerySet(models.QuerySet):
    def aprobados(self):
        return self.filter(estado='aprobado')

    def pendientes(self):
        return self.filter(estado='pendiente')

    def rechazados(self):
        return self.filter(estado='rechazado')

    def sustentados(self):
        return self.exclude(nota='')

    def activos(self):
        return self.filter(fecha_entrega__year=datetime.now().year)

    def sustentacion_pendiente(self):
        return self.filter(fecha_sustentacion__year=datetime.now().year)

    def anteproyectos(self):
        return self.exclude(estado='rechazado')

    def licenciatura(self):
        return self.filter(programa='licenciatura')

    def especializacion(self):
        return self.filter(programa='especializacion')

    def maestria(self):
        return self.filter(programa='maestria')

    def doctorado(self):
        return self.filter(programa='doctorado')

    def facultad(self, facultad):
        return self.filter(facultad_id=facultad)

    def escuela(self, escuela):
        return self.filter(escuela_id=escuela)

    def carrera(self, carrera):
        return self.filter(carrera_id=carrera)


class TrabajoManager(models.Manager):
    def get_queryset(self):
        return TrabajoQuerySet(self.model, using=self._db)

    def aprobados(self):
        return self.get_queryset().aprobados()

    def activos(self):
        return self.get_queryset().activos()

    def sustentacion_pendiente(self):
        return self.get_queryset().sustentacion_pendiente()

    def anteproyectos(self):
        return self.get_queryset().anteproyectos()

    def pendientes(self):
        return self.get_queryset().pendientes()

    def rechazados(self):
        return self.get_queryset().rechazados()

    def licenciatura(self):
        return self.get_queryset().licenciatura()

    def especializacion(self):
        return self.get_queryset().especializacion()

    def maestria(self):
        return self.get_queryset().maestria()

    def doctorado(self):
        return self.get_queryset().doctorado()

    def facultad(self, facultad):
        return self.get_queryset().facultad(facultad)

    def escuela(self, escuela):
        return self.get_queryset().escuela(escuela)

    def carrera(self, carrera):
        return self.get_queryset().carrera(carrera)

    def sustentados(self):
        return self.get_queryset().sustentados()
