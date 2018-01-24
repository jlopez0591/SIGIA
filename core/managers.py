from django.db import models

class PersonManager(models.Manager):
    def profesores(self):
        return self.filter(groups__name='Profesores')