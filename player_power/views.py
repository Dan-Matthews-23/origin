from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
#from django.contrib.auth.models import User
#from military.models import Troops
#from user_account.models import UserProfile
from faction_data.models import TroopAttributes
#from .models import PlayerPower
from game_settings.views import get_troops, get_user, get_power, get_troop_attributes, get_bonus


def calculate_attack(request, user):
    user = get_user(request)    
    power = get_power(request, user)
    troops = get_troops(request, user)
    attributes = get_troop_attributes(request)
    faction = "Amazons"#user.faction
    get_bonus_data = get_bonus(request)
    plus_bonus = 0
    
    try:
        attack_bonus = get_bonus_data[faction]["Attack"]
        #defence_bonus = get_bonus_data[faction]["Defence"]
        #intel_bonus = get_bonus_data[faction]["Intel"]
        #income_bonus = get_bonus_data[faction]["Income"]
        #print(f"Attack Bonus is {attack_bonus}, Defence Bonus is {defence_bonus}, Intel Bonus is {intel_bonus}, Income Bonus ios {income_bonus}")
        print(f"Attack Bonus is {attack_bonus}")
    except KeyError:
        attack_bonus = 0
        print(f"Possible key error. Attack Bonus is {attack_bonus}") 
    total_attack_power = (
        troops.weak_attack_troops * int(attributes['attack_tier_one_power']) +
        troops.strong_attack_troops * int(attributes['attack_tier_two_power']) +
        troops.elite_attack_troops * int(attributes['attack_tier_three_power'])
    )
    plus_bonus = ((total_attack_power/100)*attack_bonus)+total_attack_power
    try:        
        power.attack = plus_bonus
        power.save()
    except power.DoesNotExist:       
        new_power = PlayerPower.objects.create(
            user_profile=request.user,
            attack=plus_bonus,            
        )
    return plus_bonus    

 



def calculate_defence(request, user):    
    power = get_power(request, user)
    troops = get_troops(request, user)
    attributes = get_troop_attributes(request)
    faction = "Amazons"#user.faction
    get_bonus_data = get_bonus(request)
    plus_bonus = 0
    
    try:
        defence_bonus = get_bonus_data[faction]["Defence"]           
        
        #print(f"Attack Bonus is {defence_bonus}, Defence Bonus is {defence_bonus}, Intel Bonus is {intel_bonus}, Income Bonus ios {income_bonus}")
        print(f"Defence Bonus is {defence_bonus}")
    except KeyError:
        defence_bonus = 0
        print(f"Possible key error. Defence Bonus is {defence_bonus}") 
    total_defence_power = (
        troops.weak_defence_troops * int(attributes['defence_tier_one_power']) +
        troops.strong_defence_troops * int(attributes['defence_tier_two_power']) +
        troops.elite_defence_troops * int(attributes['defence_tier_three_power'])
    )
    plus_bonus = ((total_defence_power/100)*defence_bonus)+total_defence_power
    try:        
        power.defence = plus_bonus
        power.save()
    except power.DoesNotExist:       
        new_power = PlayerPower.objects.create(
            user_profile=request.user,
            defence=plus_bonus,            
        )
    return plus_bonus







def calculate_intel(request, user):    
    power = get_power(request, user)
    troops = get_troops(request, user)
    attributes = get_troop_attributes(request)
    faction = "Amazons"#user.faction
    get_bonus_data = get_bonus(request)
    plus_bonus = 0
    
    try:
        intel_bonus = get_bonus_data[faction]["Intel"]
        #intel_bonus = get_bonus_data[faction]["Intel"]
        #intel_bonus = get_bonus_data[faction]["Intel"]
        #income_bonus = get_bonus_data[faction]["Income"]
        #print(f"Attack Bonus is {intel_bonus}, Intel Bonus is {intel_bonus}, Intel Bonus is {intel_bonus}, Income Bonus ios {income_bonus}")
        print(f"Intel Bonus is {intel_bonus}")
    except KeyError:
        intel_bonus = 0
        print(f"Possible key error. Intel Bonus is {intel_bonus}") 
    total_intel_power = (
        troops.weak_intel_troops * int(attributes['intel_tier_one_power']) +
        troops.strong_intel_troops * int(attributes['intel_tier_two_power']) +
        troops.elite_intel_troops * int(attributes['intel_tier_three_power'])
    )
    plus_bonus = ((total_intel_power/100)*intel_bonus)+total_intel_power
    try:        
        power.intel = plus_bonus
        power.save()
    except power.DoesNotExist:       
        new_power = PlayerPower.objects.create(
            user_profile=request.user,
            intel=plus_bonus,            
        )
    return plus_bonus




def calculate_income(request, user):    
    power = get_power(request, user)
    troops = get_troops(request, user)
    attributes = get_troop_attributes(request)
    faction = "Amazons"#user.faction
    get_bonus_data = get_bonus(request)
    plus_bonus = 0
    
    try:
        income_bonus = get_bonus_data[faction]["Income"]
        #income_bonus = get_bonus_data[faction]["Income"]
        #income_bonus = get_bonus_data[faction]["Income"]
        #income_bonus = get_bonus_data[faction]["Income"]
        #print(f"Income Bonus is {income_bonus}, Income Bonus is {income_bonus}, Income Bonus is {income_bonus}, Income Bonus ios {income_bonus}")
        print(f"Income Bonus is {income_bonus}")
    except KeyError:
        income_bonus = 0
        print(f"Possible key error. Income Bonus is {income_bonus}") 
    total_income_power = (
        troops.income_specialists * int(attributes['income_specialist_power'])        
    )
    plus_bonus = ((total_income_power/100)*income_bonus)+total_income_power
    try:        
        power.income = plus_bonus
        power.save()
    except power.DoesNotExist:       
        new_power = PlayerPower.objects.create(
            user_profile=request.user,
            income=plus_bonus,            
        )
    return plus_bonus













