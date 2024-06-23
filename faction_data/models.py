from django.db import models
from django.conf import settings



class TroopAttributes(models.Model):    
    attack_tier_one_name = models.CharField(null=False, blank=False, default="Operation Recruit", max_length=50)
    attack_tier_one_power = models.IntegerField(null=False, blank=False, default=10)
    attack_tier_one_cost = models.IntegerField(null=False, blank=False, default=100)
    attack_tier_two_name = models.CharField(null=False, blank=False, default="Operation Platoon", max_length=50)
    attack_tier_two_power = models.IntegerField(null=False, blank=False, default=100)
    attack_tier_two_cost = models.IntegerField(null=False, blank=False, default=1000)
    attack_tier_three_name = models.CharField(null=False, blank=False, default="Operation Regiment", max_length=50)
    attack_tier_three_power = models.IntegerField(null=False, blank=False, default=1000)
    attack_tier_three_cost = models.IntegerField(null=False, blank=False, default=10000)
    defence_tier_one_name = models.CharField(null=False, blank=False, default="Defending Recruit", max_length=50)
    defence_tier_one_power = models.IntegerField(null=False, blank=False, default=10)
    defence_tier_one_cost = models.IntegerField(null=False, blank=False, default=100)
    defence_tier_two_name = models.CharField(null=False, blank=False, default="Defending Platoon", max_length=50)
    defence_tier_two_power = models.IntegerField(null=False, blank=False, default=100)
    defence_tier_two_cost = models.IntegerField(null=False, blank=False, default=1000)
    defence_tier_three_name = models.CharField(null=False, blank=False, default="Defending Regiment", max_length=50)
    defence_tier_three_power = models.IntegerField(null=False, blank=False, default=1000)
    defence_tier_three_cost = models.IntegerField(null=False, blank=False, default=10000)
    intel_tier_one_name = models.CharField(null=False, blank=False, default="Trainee Covert Officer", max_length=50)
    intel_tier_one_power = models.IntegerField(null=False, blank=False, default=10)
    intel_tier_one_cost = models.IntegerField(null=False, blank=False, default=100)
    intel_tier_two_name = models.CharField(null=False, blank=False, default="Covert Officer", max_length=50)
    intel_tier_two_power = models.IntegerField(null=False, blank=False, default=100)
    intel_tier_two_cost = models.IntegerField(null=False, blank=False, default=1000)
    intel_tier_three_name = models.CharField(null=False, blank=False, default="Distinguished Covert Officer", max_length=50)
    intel_tier_three_power = models.IntegerField(null=False, blank=False, default=1000)
    intel_tier_three_cost = models.IntegerField(null=False, blank=False, default=10000)
    income_specialist_name = models.CharField(null=False, blank=False, default="Income Specialist", max_length=50)
    income_specialist_power = models.IntegerField(null=False, blank=False, default=1000)
    income_specialist_cost = models.IntegerField(null=False, blank=False, default=10000)
    untrained_name = models.CharField(null=False, blank=False, default="Untrained Unit", max_length=50)
    untrained_cost = models.IntegerField(null=False, blank=False, default=0)
    untrained_power = models.IntegerField(null=False, blank=False, default=0)
    




   
    
