from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from military.models import Troops
from user_account.models import UserProfile
from faction_data.models import TroopAttributes

def calculate_attack(request):
  profile = UserProfile.objects.get(user=request.user)
  troops = Troops.objects.get(user_profile=profile)  
  total_attack_power = (
      troops.weak_attack_troops * TroopAttributes.objects.get().attack_tier_one_power +
      troops.strong_attack_troops * TroopAttributes.objects.get().attack_tier_two_power +
      troops.elite_attack_troops * TroopAttributes.objects.get().attack_tier_three_power
  )
  return total_attack_power


def calculate_defence(request):
    profile = UserProfile.objects.get(user=request.user)
    troops = Troops.objects.get(user_profile=profile)  
    total_defence_power = (
        troops.weak_defence_troops * TroopAttributes.objects.get().defence_tier_one_power +
        troops.strong_defence_troops * TroopAttributes.objects.get().defence_tier_two_power +
        troops.elite_defence_troops * TroopAttributes.objects.get().defence_tier_three_power
    )
    return total_defence_power


def calculate_intel(request):
    profile = UserProfile.objects.get(user=request.user)
    troops = Troops.objects.get(user_profile=profile)  
    total_intel_power = (
        troops.weak_intel_troops * TroopAttributes.objects.get().intel_tier_one_power +
        troops.strong_intel_troops * TroopAttributes.objects.get().intel_tier_two_power +
        troops.elite_intel_troops * TroopAttributes.objects.get().intel_tier_three_power
    )
    return total_intel_power

def calculate_income(request):
    profile = UserProfile.objects.get(user=request.user)
    troops = Troops.objects.get(user_profile=profile)  
    total_income_power = (       
        troops.income_specialists * TroopAttributes.objects.get().income_specialist_power
    )
    return total_income_power
