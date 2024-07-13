from django.db import models
from user_account.models import UserProfile

class TechnologyCategory(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Civilization(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name






class ResearchableTechnology(models.Model):
    name = models.CharField(max_length=80, unique=True)
    category = models.ForeignKey(TechnologyCategory, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    is_unique = models.BooleanField(default=False)
    unique_to = models.ForeignKey(Civilization, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name




class UserTechnology(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='technologies')
    technology = models.ForeignKey(ResearchableTechnology, on_delete=models.CASCADE)
    research_completed = models.BooleanField(default=False)
    research_points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user_profile.username} - {self.technology.name}"  # Example string representation

