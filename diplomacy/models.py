from django.db import models
from user_account.models import UserProfile


RELATION_CHOICES = (
    ("Ally", "Ally"),
    ("Neutral", "Neutral"),
    ("Enemy", "Enemy"),   
)




class Diplomacy(models.Model):    
    date = models.DateTimeField(auto_now_add=True)    
    target = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='target_diplomacy')   
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='user_diplomacy')
    relation = models.CharField(max_length=20, choices=RELATION_CHOICES, default="Neutral")
    
