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



# class AnteproyectoQuerySet(models.QuerySet):
#     def aprobados(self):
#         return self.filter(estado='aprobado')

#     def rechazados(self):
#         return self.filter(estado='rechazado')

#     def pendientes(self):
#         return self.filter(estado='pendiente')

#     def pertenece_a(self, estudiante):
#         return self.filter(estudiante=estudiante)

#     def puede_aprobar(self, usuario):
#         escuela_usuario = usuario.perfil.escuela
#         return self.filter(escuela=escuela_usuario, estado='pendiente')

#     def facultad(self, usuario):
#         facultad = usuario.perfil.unidad
#         return self.filter(unidad=facultad, estado='pendiente')

#     def escuela(self, usuario):
#         escuela = usuario.perfil.escuela
#         return self.filter(escuela=escuela)


# class AnteproyectoManager(models.Manager):
#     def get_queryset(self):
#         return AnteproyectoQuerySet(self.model, using=self._db)

#     def aprobados(self):
#         return self.get_queryset().aprobados()

#     def rechazados(self):
#         return self.get_queryset().rechazados()

#     def pendientes(self):
#         return self.get_queryset().pendientes()

#     def pertenece_a(self, estudiante):
#         return self.get_queryset().pertenece_a(estudiante=estudiante)

#     def puede_aprobar(self, usuario):
#         return self.get_queryset().puede_aprobar(usuario=usuario)

#     def facultad(self, usuario):
#         return self.get_queryset().facultad(usuario=usuario)

#     def escuela(self, usuario):
#         return self.get_queryset().escuela(usuario=usuario)


# class ProyectoQueryset(models.QuerySet):

#     def facultad(self, facultad):
#         return self.filter(unidad=facultad)


# class ProyectoManager(models.Manager):

#     def get_queryset(self):
#         return ProyectoQueryset(self.model, using=self._db)
