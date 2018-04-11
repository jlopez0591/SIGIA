# from django.db import models
#
#
# class PersonManager(models.Manager):
#     def profesores(self):
#         return self.filter(groups__name='Profesores')
#
#
# class PerfilQuerySet(models.QuerySet):
#     def profesores(self):
#         return self.filter(usuario__groups__name='Profesores')
#
#
# class PerfilManager(models.Manager):
#     def get_queryset(self):
#         return PerfilQuerySet(self.model, using=self._db)
#
#     def profesores(self):
#         return self.get_queryset().profesores()
