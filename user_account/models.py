from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from .models import Production


FACTION_CHOICES = (
    ("amazons", "Amazons"),
    ("spartans", "Spartans"),
    ("atlantians", "Atlantians"),
    ("witches", "Witches"),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=80, null=True, blank=True)
    email = models.CharField(max_length=80, null=True, blank=True)
    faction = models.CharField(max_length=20, choices=FACTION_CHOICES)
    


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

"""
@receiver(post_save, sender=User)
def create_production_profile(sender, instance, created, **kwargs):
    if created:
        Production.objects.create(user=instance)"""