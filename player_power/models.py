from django.db import models
from django.db.models import Sum
from django.conf import settings
from user_account.models import UserProfile


class PlayerPower(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='player_power')
    attack = models.IntegerField(null=False, blank=False, default=0)
    defence = models.IntegerField(null=False, blank=False, default=0)
    intel = models.IntegerField(null=False, blank=False, default=0)
    income = models.IntegerField(null=False, blank=False, default=0)