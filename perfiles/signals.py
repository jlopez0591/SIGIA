# Django
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Third party
from perfiles.models import Perfil


# Metodos para la creacion de perfiles con la creacion de usuarios
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()
