from django.db import models
from polymorphic.manager import PolymorphicManager


class ActividadQuerySet(models.QuerySet):
    def en_espera(self):
        return self.filter(estado='espera')

    def rechazado(self):
        return self.filter(estado='rechazado')

    def aprobado(self):
        return self.filter(estado='aprobado')

    def puede_aprobar(self, usuario):
        return self.filter(estado='espera', departamento=usuario.perfil.departamento)

    def propias(self, usuario):
        return self.filter(usuario=usuario)


class ActividadManager(PolymorphicManager):
    def get_queryset(self):
        return ActividadQuerySet(self.model, using=self._db)

    def en_espera(self):
        return self.get_queryset().en_espera()

    def rechazado(self):
        return self.get_queryset().rechazado()

    def aprobado(self):
        return self.get_queryset().aprobado()

    def puede_aprobar(self, usuario):
        return self.get_queryset().puede_aprobar(usuario)

    def propias(self, usuario):
        return self.get_queryset().propias(usuario)