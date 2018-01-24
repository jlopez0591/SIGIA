# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from actividades.models import Notificacion
#
# @receiver(post_save, sender=Notificacion)
# def crear_notificacion(sender, instance, created, **kwargs):
#     if created:
#         Notificacion.objects.create(usuario=u)
