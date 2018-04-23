from django.db import models


class UsuarioQuerySet(models.QuerySet):
    def profesores(self):
        return self.filter(groups__name='Profesores'.title())

    def decanos(self):
        return self.filter(groups__name='Decanos'.title())

    def departamento(self):
        return self.filter(groups__name='Director de Depatamento'.title())

    def escuela(self):
        return self.filter(groups__name='Director de Escuela'.title())

    def administrativos(self):
        return self.filter(groups__name='Administrativos'.title())

    def comision(self):
        return self.filter(groups__name='Comision de Anteproyecto'.title())


class UsuarioManager(models.Manager):
    def get_queryset(self):
        return UsuarioQuerySet(self.model, using=self._db)

    def profesores(self):
        return self.get_queryset().profesores()

    def decanos(self):
        return self.get_queryset().decanos()

    def departamento(self):
        return self.get_queryset().departamento()

    def escuela(self):
        return self.get_queryset().escuela()

    def administrativos(self):
        return self.get_queryset().administrativos()

    def comision(self):
        return self.get_queryset().comision()
