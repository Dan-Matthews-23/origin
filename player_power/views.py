from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
#from django.contrib.auth.models import User
#from military.models import Troops
#from user_account.models import UserProfile
from faction_data.models import TroopAttributes
#from .models import PlayerPower
from game_settings.views import get_troops, get_user, get_power, get_troop_attributes


def calculate_attack(request, user):    
    power = get_power(request, user)
    troops = get_troops(request, user)
    attributes = get_troop_attributes(request)    
    total_attack_power = (
        troops.weak_attack_troops * int(attributes['attack_tier_one_power']) +
        troops.strong_attack_troops * int(attributes['attack_tier_two_power']) +
        troops.elite_attack_troops * int(attributes['attack_tier_three_power'])
    )
    try:        
        power.attack = total_attack_power
        power.save()
    except power.DoesNotExist:       
        new_power = PlayerPower.objects.create(
            user_profile=request.user,
            attack=total_attack_power,            
        )
    return total_attack_power    

 



def calculate_defence(request, user):    
    power = get_power(request, user)
    troops = get_troops(request, user)
    attributes = get_troop_attributes(request)
    total_defence_power = (
        troops.weak_defence_troops * int(attributes['defence_tier_one_power']) +
        troops.strong_defence_troops * int(attributes['defence_tier_two_power']) +
        troops.elite_defence_troops * int(attributes['defence_tier_three_power'])
    )
    try:        
        power.defence = total_defence_power
        power.save()
    except power.DoesNotExist:       
        new_power = PlayerPower.objects.create(
            user_profile=request.user,
            defence=total_defence_power,            
        )
    return total_defence_power







def calculate_intel(request, user):    
    power = get_power(request, user)
    troops = get_troops(request, user)
    attributes = get_troop_attributes(request)
    total_intel_power = (
        troops.weak_intel_troops * int(attributes['intel_tier_one_power']) +
        troops.strong_intel_troops * int(attributes['intel_tier_two_power']) +
        troops.elite_intel_troops * int(attributes['intel_tier_three_power'])
    )
    try:        
        power.intel = total_intel_power
        power.save()
    except power.DoesNotExist:       
        new_power = PlayerPower.objects.create(
            user_profile=request.user,
            intel=total_intel_power,            
        )
    return total_intel_power




def calculate_income(request, user):    
    power = get_power(request, user)
    troops = get_troops(request, user)
    attributes = get_troop_attributes(request)
    total_income_power = (
        troops.income_specialists * int(attributes['income_specialist_power'])        
    )
    try:        
        power.income = total_income_power
        power.save()
    except power.DoesNotExist:       
        new_power = PlayerPower.objects.create(
            user_profile=request.user,
            income=total_income_power,            
        )
    return total_income_power













