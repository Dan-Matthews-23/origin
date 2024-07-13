from django.db import models
from django.db.models import Sum
from django.conf import settings
from user_account.models import UserProfile


RESULT_CHOICES = (
    ("Won", "Won"),
    ("Lost", "Lost"),
    
)

class IntelLog(models.Model):
    result = models.CharField(max_length=20, choices=RESULT_CHOICES)
    defender_user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='defender_profile')    
    defender_intel = models.IntegerField(null=False, blank=False, default=0)
    defender_troops = models.IntegerField(null=False, blank=False, default=0)
    defender_technologies = models.IntegerField(null=False, blank=False, default=0)
    defender_bonus = models.IntegerField(null=False, blank=False, default=0)
    attacker_user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='attacker_profile')   
    attacker_intel = models.IntegerField(null=False, blank=False, default=0)
    attacker_troops = models.IntegerField(null=False, blank=False, default=0)
    attacker_technologies = models.IntegerField(null=False, blank=False, default=0)
    attacker_bonus = models.IntegerField(null=False, blank=False, default=0)

    