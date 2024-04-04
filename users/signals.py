from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save,sender=User)  #when a user is saved send this signal
def create_profiel(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)  #when a user is saved send this signal
def create_profiel(sender, instance, **kwargs): #kwargs accepts any additional keyword args towards the end
    instance.profile.save()