from django.db import models
from django.db.models import Sum
from django.conf import settings
from user_account.models import UserProfile


class Technology(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='technology')
    tech_level = models.IntegerField(null=False, blank=False, default=0)
    