from django.db import models
from django.db.models import Sum
from django.conf import settings
from user_account.models import UserProfile


class Production(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='production')
    pop_growth = models.IntegerField(null=False, blank=False, default=10)
    knowledge_points = models.IntegerField(null=False, blank=False, default=10)
    knowledge_points_growth = models.IntegerField(null=False, blank=False, default=0)
    income = models.IntegerField(null=False, blank=False, default=10)
    data_crystal_balance = models.IntegerField(null=False, blank=False, default=10)