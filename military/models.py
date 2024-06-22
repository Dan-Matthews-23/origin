from django.db import models
from django.db.models import Sum
from django.conf import settings
from user_account.models import UserProfile


class Troops(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='military')
    weak_attack_troops = models.IntegerField(null=False, blank=False, default=10)
    strong_attack_troops = models.IntegerField(null=False, blank=False, default=10)
    elite_attack_troops = models.IntegerField(null=False, blank=False, default=10)
    weak_defence_troops = models.IntegerField(null=False, blank=False, default=10)
    strong_defence_troops = models.IntegerField(null=False, blank=False, default=10)
    elite_defence_troops = models.IntegerField(null=False, blank=False, default=10)
    weak_intel_troops = models.IntegerField(null=False, blank=False, default=10)
    strong_intel_troops = models.IntegerField(null=False, blank=False, default=10)
    elite_intel_troops = models.IntegerField(null=False, blank=False, default=10)
    income_specialists = models.IntegerField(null=False, blank=False, default=10)
    untrained_units = models.IntegerField(null=False, blank=False, default=10)
    
