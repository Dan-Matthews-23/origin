from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from military.models import Troops
from user_account.models import UserProfile
from faction_data.models import TroopAttributes
from .models import PlayerPower

def calculate_attack(requestl, player_id):
    profile = UserProfile.objects.get(id=player_id)
    troops = Troops.objects.get(user_profile=profile)
    total_attack_power = (
        troops.weak_attack_troops * TroopAttributes.objects.get().attack_tier_one_power +
        troops.strong_attack_troops * TroopAttributes.objects.get().attack_tier_two_power +
        troops.elite_attack_troops * TroopAttributes.objects.get().attack_tier_three_power
  )
    try:
        update_attack = PlayerPower.objects.get(user_profile=profile)
        update_attack.attack = total_attack_power
        update_attack.save()
    except PlayerPower.DoesNotExist:       
        new_power = PlayerPower.objects.create(
            user_profile=profile,
            attack=total_attack_power,
            
        )     
    all_players = PlayerPower.objects.all().order_by('-attack')
    update_attack.attack_rank = all_players.filter(attack__gt=update_attack.attack).count() + 1   
    update_attack.attack = total_attack_power
    update_attack.save()
    return total_attack_power



def calculate_defence(request, player_id):
    profile = UserProfile.objects.get(id=player_id)
    troops = Troops.objects.get(user_profile=profile)
    total_defence_power = (
        troops.weak_defence_troops * TroopAttributes.objects.get().defence_tier_one_power +
        troops.strong_defence_troops * TroopAttributes.objects.get().defence_tier_two_power +
        troops.elite_defence_troops * TroopAttributes.objects.get().defence_tier_three_power
  )
    try:
        update_defence = PlayerPower.objects.get(user_profile=profile)
        update_defence.defence = total_defence_power
        update_defence.save()
    except PlayerPower.DoesNotExist:       
        new_power = PlayerPower.objects.create(
            user_profile=profile,
            defence=total_defence_power,
            
        )     
    all_players = PlayerPower.objects.all().order_by('-defence')
    update_defence.defence_rank = all_players.filter(defence__gt=update_defence.defence).count() + 1   
    update_defence.defence = total_defence_power
    update_defence.save()
    return total_defence_power






def calculate_intel(request):
    profile = UserProfile.objects.get(user=request.user)
    troops = Troops.objects.get(user_profile=profile)
    total_intel_power = (
        troops.weak_intel_troops * TroopAttributes.objects.get().intel_tier_one_power +
        troops.strong_intel_troops * TroopAttributes.objects.get().intel_tier_two_power +
        troops.elite_intel_troops * TroopAttributes.objects.get().intel_tier_three_power
  )
    try:
        update_intel = PlayerPower.objects.get(user_profile=profile)
        update_intel.intel = total_intel_power
        update_intel.save()
    except PlayerPower.DoesNotExist:       
        new_power = PlayerPower.objects.create(
            user_profile=profile,
            intel=total_intel_power,
            
        )     
    all_players = PlayerPower.objects.all().order_by('-intel')
    update_intel.intel_rank = all_players.filter(intel__gt=update_intel.intel).count() + 1   
    update_intel.intel = total_intel_power
    update_intel.save()
    return total_intel_power




def calculate_income(request):
    profile = UserProfile.objects.get(user=request.user)
    troops = Troops.objects.get(user_profile=profile)
    total_income_power = (       
        troops.income_specialists * TroopAttributes.objects.get().income_specialist_power
  )
    try:
        update_income = PlayerPower.objects.get(user_profile=profile)
        update_income.income = total_income_power
        update_income.save()
    except PlayerPower.DoesNotExist:       
        new_power = PlayerPower.objects.create(
            user_profile=profile,
            income=total_income_power,
            
        )     
    all_players = PlayerPower.objects.all().order_by('-income')
    update_income.income_rank = all_players.filter(income__gt=update_income.income).count() + 1   
    update_income.income = total_income_power
    update_income.save()
    return total_income_power













