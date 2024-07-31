from django.db import models
from user_account.models import UserProfile


RELATION_CHOICES = (
    ("Ally", "Ally"),
    ("Neutral", "Neutral"),
    ("Enemy", "Enemy"),   
)

EVENT_CHOICES = (
    ("You attacked", "You attacked"),
    ("They attacked you", "They attacked you"),    
    ("You proposed an alliance", "You proposed an alliance"),   
    ("They proposed an alliance", "They proposed an alliance"),    
    ("You accepted an alliance proposal", "You accepted an alliance proposal"),
    ("They accepted an alliance proposal", "They accepted an alliance proposal"),
    ("You rejected an alliance proposal", "You rejected an alliance proposal"),
    ("They rejected an alliance proposal", "They rejected an alliance proposal"),    
    ("You proposed a Non-Aggression Pact", "You proposed a Non-Aggression Pact"),
    ("They proposed a Non-Aggression Pact", "They proposed a Non-Aggression Pact"),   
    ("You accepted a Non-Aggression Pact proposal", "You accepted a Non-Aggression Pact proposal"),
    ("They accepted a Non-Aggression Pact proposal", "They accepted a Non-Aggression Pact proposal"),
    ("You rejected a Non-Aggression Pact proposal", "You rejected a Non-Aggression Pact proposal"),
    ("They rejected a Non-Aggression Pact proposal", "They rejected a Non-Aggression Pact proposal"),    
    ("You declared war", "You declared war"),
    ("They declared war", "They declared war"),
    ("Your Non-Aggression Pact expired", "Your Non-Aggression Pact expired"),
    ("You ended your alliance", "You ended your alliance"),
    ("They ended your alliance", "They ended your alliance"),
    ("You set your relations to neutral", "You set your relations to neutral"),
    ("They set your relations to neutral", "They set your relations to neutral"),
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


class NonAggression(models.Model):    
    date = models.DateTimeField(auto_now_add=True)    
    target = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='target_non_agg')
    target_accepted = models.BooleanField(null=False, blank=False, default=False) 
    target_rejected = models.BooleanField(null=False, blank=False, default=False) 
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='user_non_agg')
    user_accepted = models.BooleanField(null=False, blank=False, default=False)
    user_rejected = models.BooleanField(null=False, blank=False, default=False) 
    length = models.IntegerField(null=False, blank=False, default=1440)#30 days
    expired = models.BooleanField(null=False, blank=False, default=False)


class DiplomaticTimeline(models.Model):    
    date = models.DateTimeField(auto_now_add=True)    
    target = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='target_timeline')   
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='user_timeline')    
    event_message_user = models.CharField(max_length=500, choices=EVENT_CHOICES)  
    event_message_target = models.CharField(max_length=500, choices=EVENT_CHOICES)
    
   

    
