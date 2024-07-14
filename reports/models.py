from django.db import models
from django.db.models import Sum
from django.conf import settings
from user_account.models import UserProfile


RESULT_CHOICES = (
    ("Overwhelming Victory", "Overwhelming Victory"),
    ("Clear Victory", "Clear Victory"),
    ("Victory", "Victory"),
    ("Loss", "Loss"),
    ("Clear Loss", "Clear Loss"),
    ("Overwhelming Loss", "Overwhelming Loss"),
    
)

class IntelLog(models.Model):
    report_id = models.AutoField(primary_key=True, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=20, choices=RESULT_CHOICES)
    defender_user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='defender_profile')    
    defender_intel = models.IntegerField(null=False, blank=False, default=0)
    defender_troops = models.IntegerField(null=False, blank=False, default=0)
    defender_technologies = models.IntegerField(null=False, blank=False, default=0)
    defender_bonus = models.IntegerField(null=False, blank=False, default=0)
    defender_weak_intel_troops_loss = models.IntegerField(null=False, blank=False, default=0)
    defender_strong_intel_troops_loss = models.IntegerField(null=False, blank=False, default=0)
    defender_elite_intel_troops_loss = models.IntegerField(null=False, blank=False, default=0)
    attacker_user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='attacker_profile')   
    attacker_intel = models.IntegerField(null=False, blank=False, default=0)
    attacker_troops = models.IntegerField(null=False, blank=False, default=0)
    attacker_technologies = models.IntegerField(null=False, blank=False, default=0)
    attacker_bonus = models.IntegerField(null=False, blank=False, default=0)
    attacker_weak_intel_troops_loss = models.IntegerField(null=False, blank=False, default=0)
    attacker_strong_intel_troops_loss = models.IntegerField(null=False, blank=False, default=0)
    attacker_elite_intel_troops_loss = models.IntegerField(null=False, blank=False, default=0)
    defender_defence_power = models.IntegerField(null=False, blank=False, default=0)
    defender_attack_power = models.IntegerField(null=False, blank=False, default=0)
    defender_intel_power = models.IntegerField(null=False, blank=False, default=0)
    defender_income_power = models.IntegerField(null=False, blank=False, default=0)
    defender_weak_attack_troops = models.IntegerField(null=False, blank=False, default=10)
    defender_strong_attack_troops = models.IntegerField(null=False, blank=False, default=10)
    defender_elite_attack_troops = models.IntegerField(null=False, blank=False, default=10)
    defender_weak_defence_troops = models.IntegerField(null=False, blank=False, default=10)
    defender_strong_defence_troops = models.IntegerField(null=False, blank=False, default=10)
    defender_elite_defence_troops = models.IntegerField(null=False, blank=False, default=10)
    defender_weak_intel_troops = models.IntegerField(null=False, blank=False, default=10)
    defender_strong_intel_troops = models.IntegerField(null=False, blank=False, default=10)
    defender_elite_intel_troops = models.IntegerField(null=False, blank=False, default=10)
    defender_income_specialists = models.IntegerField(null=False, blank=False, default=10)
    defender_untrained_units = models.IntegerField(null=False, blank=False, default=10)
    




  

    