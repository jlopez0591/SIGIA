from datetime import datetime

from django.db import models


class EstudianteQuerySet(models.QuerySet):
    def activos(self):
        return self.filter(ultimo_anio=datetime.now().year)

    def hombres(self):
        return self.filter(ultimo_anio=datetime.now().year)

    def mujeres(self):
        return self.filter(ultimo_anio=datetime.now().year)


class EstudianteManager(models.Manager):
    def get_queryset(self):
        return EstudianteQuerySet(self.model, using=self._db)

    def activos(self):
        return self.get_queryset().activos()

    def hombres(self):
        return self.get_queryset().hombres()

    def mujeres(self):
        return self.get_queryset().mujeres()


class AnteproyectoQuerySet(models.QuerySet):
    def aprobados(self):
        return self.filter(estado='aprobado')

    def rechazados(self):
        return self.filter(estado='rechazado')

    def pendientes(self):
        return self.filter(estado='pendiente')

    def pertenece_a(self, estudiante):
        return self.filter(estudiante=estudiante)

    def puede_aprobar(self, usuario):
        escuela_usuario = usuario.perfil.escuela
        return self.filter(seccion=escuela_usuario, estado='pendiente')


class AnteproyectoManager(models.Manager):
    def get_queryset(self):
        return AnteproyectoQuerySet(self.model, using=self._db)

    def aprobados(self):
        return self.get_queryset().aprobados()

    def rechazados(self):
        return self.get_queryset().rechazados()

    def pendientes(self):
        return self.get_queryset().pendientes()

    def pertenece_a(self, estudiante):
        return self.get_queryset().pertenece_a(estudiante=estudiante)

    def puede_aprobar(self, usuario):
        return self.get_queryset().puede_aprobar(usuario=usuario)
