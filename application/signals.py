from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# The user will be what we call the 'sender' since its going to be sending the signal
# The reciever will be a function that gets the signal then performs some tasks
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()