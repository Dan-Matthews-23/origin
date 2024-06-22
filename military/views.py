from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from .models import Troops
from user_account.models import UserProfile
from user_account.forms import UserProfileForm
from django.contrib import messages
from django.conf import settings
from faction_data.models import TroopAttributes
#rom home.faction_data import military_units




def getTroopAttributes(request):
    getTroopAttributes = TroopAttributes.objects.get()    
    attack_tier_one_name = getTroopAttributes.attack_tier_one_name
    attack_tier_one_power = getTroopAttributes.attack_tier_one_power
    attack_tier_one_cost = getTroopAttributes.attack_tier_one_cost
    attack_tier_two_name = getTroopAttributes.attack_tier_two_name
    attack_tier_two_power = getTroopAttributes.attack_tier_two_power
    attack_tier_two_cost = getTroopAttributes.attack_tier_two_cost
    attack_tier_three_name = getTroopAttributes.attack_tier_three_name
    attack_tier_three_power = getTroopAttributes.attack_tier_three_power
    attack_tier_three_cost = getTroopAttributes.attack_tier_three_cost
    defence_tier_one_name = getTroopAttributes.defence_tier_one_name
    defence_tier_one_power = getTroopAttributes.defence_tier_one_power
    defence_tier_one_cost = getTroopAttributes.defence_tier_one_cost
    defence_tier_two_name = getTroopAttributes.defence_tier_two_name
    defence_tier_two_power = getTroopAttributes.defence_tier_two_power
    defence_tier_two_cost = getTroopAttributes.defence_tier_two_cost
    defence_tier_three_name = getTroopAttributes.defence_tier_three_name
    defence_tier_three_power = getTroopAttributes.defence_tier_three_power
    defence_tier_three_cost = getTroopAttributes.defence_tier_three_cost
    intel_tier_one_name = getTroopAttributes.intel_tier_one_name
    intel_tier_one_power = getTroopAttributes.intel_tier_one_power
    intel_tier_one_cost = getTroopAttributes.intel_tier_one_cost
    intel_tier_two_name = getTroopAttributes.intel_tier_two_name
    intel_tier_two_power = getTroopAttributes.intel_tier_two_power
    intel_tier_two_cost = getTroopAttributes.intel_tier_two_cost
    intel_tier_three_name = getTroopAttributes.intel_tier_three_name
    intel_tier_three_power = getTroopAttributes.intel_tier_three_power
    intel_tier_three_cost = getTroopAttributes.intel_tier_three_cost
    income_specialist_name = getTroopAttributes.income_specialist_name
    income_specialist_power = getTroopAttributes.income_specialist_power
    income_specialist_cost = getTroopAttributes.income_specialist_cost    
    
    
    troopAttributes = {
            'attack_tier_one_name': attack_tier_one_name,
            'attack_tier_one_power': attack_tier_one_power,
            'attack_tier_one_cost' : attack_tier_one_cost,
            'attack_tier_two_name' : attack_tier_two_name,
            'attack_tier_two_power' : attack_tier_two_power,
            'attack_tier_two_cost' : attack_tier_two_cost,
            'attack_tier_three_name' : attack_tier_three_name,
            'attack_tier_three_power' : attack_tier_three_power,
            'attack_tier_three_cost' : attack_tier_three_cost,
            'defence_tier_one_name' : defence_tier_one_name,
            'defence_tier_one_power' : defence_tier_one_power,
            'defence_tier_one_cost' : defence_tier_one_cost,
            'defence_tier_two_name' : defence_tier_two_name,
            'defence_tier_two_power' : defence_tier_two_power,
            'defence_tier_two_cost' : defence_tier_two_cost,
            'defence_tier_three_name' : defence_tier_three_name,
            'defence_tier_three_power' : defence_tier_three_power,
            'defence_tier_three_cost' : defence_tier_three_cost,
            'intel_tier_one_name' : intel_tier_one_name,
            'intel_tier_one_power' : intel_tier_one_power,
            'intel_tier_one_cost' : intel_tier_one_cost,
            'intel_tier_two_name' : intel_tier_two_name,
            'intel_tier_two_power' : intel_tier_two_power,
            'intel_tier_two_cost' : intel_tier_two_cost,
            'intel_tier_three_name' : intel_tier_three_name,
            'intel_tier_three_power' : intel_tier_three_power,
            'intel_tier_three_cost' : intel_tier_three_cost,
            'income_specialist_name' : income_specialist_name,
            'income_specialist_power' : income_specialist_power,
            'income_specialist_cost' : income_specialist_cost,
        }
    #print(f" troopAttributes attack tier one is {troopAttributes['attack_tier_one_name']}")
    return troopAttributes
    



def military(request):  
    
    troopAttributes = getTroopAttributes(request)
    #print(troopAttributes)
    print(f" troopAttributes attack tier one is {troopAttributes['attack_tier_one_name']}")      
        
        
    
    profile = UserProfile.objects.get(user=request.user)
    try:
        troops_object = Troops.objects.get(user_profile=profile)
       
        # Render Troop Count
        weak_attack_troops = troops_object.weak_attack_troops        
        strong_attack_troops =  troops_object.strong_attack_troops
        elite_attack_troops = troops_object.elite_attack_troops
        weak_defence_troops = troops_object.weak_defence_troops
        strong_defence_troops = troops_object.strong_defence_troops
        elite_defence_troops = troops_object.elite_defence_troops
        weak_intel_troops = troops_object.weak_intel_troops
        strong_intel_troops = troops_object.strong_intel_troops
        elite_intel_troops = troops_object.elite_intel_troops
        income_specialists = troops_object.income_specialists
        untrained_units = troops_object.untrained_units    
    except Troops.DoesNotExist:       
        troops_object = Troops.objects.create(
            user_profile=profile,
            strong_attack_troops=0,
            elite_attack_troops=0,
            weak_defence_troops=0,
            strong_defence_troops=0,
            elite_defence_troops=0,
            weak_intel_troops=0,
            strong_intel_troops=0,
            elite_intel_troops=0,
            income_specialists=0,
            untrained_units=50,
        )
        weak_attack_troops = troops_object.weak_attack_troops        
        strong_attack_troops =  troops_object.strong_attack_troops
        elite_attack_troops = troops_object.elite_attack_troops
        weak_defence_troops = troops_object.weak_defence_troops
        strong_defence_troops = troops_object.strong_defence_troops
        elite_defence_troops = troops_object.elite_defence_troops
        weak_intel_troops = troops_object.weak_intel_troops
        strong_intel_troops = troops_object.strong_intel_troops
        elite_intel_troops = troops_object.elite_intel_troops
        income_specialists = troops_object.income_specialists
        untrained_units = troops_object.untrained_units    
    context = {
        'weak_attack_troops' : weak_attack_troops,      
        'strong_attack_troops':  strong_attack_troops,
        'elite_attack_troops': elite_attack_troops,
        'weak_defence_troops': weak_defence_troops,
        'strong_defence_troops' : strong_defence_troops,
        'elite_defence_troops' : elite_defence_troops,
        'weak_intel_troops' : weak_intel_troops,
        'strong_intel_troops' : strong_intel_troops,
        'elite_intel_troops' : elite_intel_troops,
        'income_specialists' : income_specialists,
        'untrained_units' : untrained_units,
    }
    return render(request, 'military/military.html', context)


