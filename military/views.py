from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from .models import Troops
from user_account.models import UserProfile
from user_account.forms import UserProfileForm
from django.contrib import messages
from django.conf import settings
from faction_data.models import TroopAttributes


def getTroopAttributes(request):
    getTroopAttributes = TroopAttributes.objects.get()    
    t1_attack_name = getTroopAttributes.attack_tier_one_name
    t1_attack_power = getTroopAttributes.attack_tier_one_power
    t1_attack_cost = getTroopAttributes.attack_tier_one_cost
    t2_attack_name = getTroopAttributes.attack_tier_two_name
    t2_attack_power = getTroopAttributes.attack_tier_two_power
    t2_attack_cost = getTroopAttributes.attack_tier_two_cost
    t3_attack_name = getTroopAttributes.attack_tier_three_name
    t3_attack_power = getTroopAttributes.attack_tier_three_power
    t3_attack_cost = getTroopAttributes.attack_tier_three_cost
    t1_defence_name = getTroopAttributes.defence_tier_one_name
    t1_defence_power = getTroopAttributes.defence_tier_one_power
    t1_defence_cost = getTroopAttributes.defence_tier_one_cost
    t2_defence_name = getTroopAttributes.defence_tier_two_name
    t2_defence_power = getTroopAttributes.defence_tier_two_power
    t2_defence_cost = getTroopAttributes.defence_tier_two_cost
    t3_defence_name = getTroopAttributes.defence_tier_three_name
    t3_defence_power = getTroopAttributes.defence_tier_three_power
    t3_defence_cost = getTroopAttributes.defence_tier_three_cost
    t1_intel_name = getTroopAttributes.intel_tier_one_name
    t1_intel_power = getTroopAttributes.intel_tier_one_power
    t1_intel_cost = getTroopAttributes.intel_tier_one_cost
    t2_intel_name = getTroopAttributes.intel_tier_two_name
    t2_intel_power = getTroopAttributes.intel_tier_two_power
    t2_intel_cost = getTroopAttributes.intel_tier_two_cost
    t3_intel_name = getTroopAttributes.intel_tier_three_name
    t3_intel_power = getTroopAttributes.intel_tier_three_power
    t3_intel_cost = getTroopAttributes.intel_tier_three_cost
    t3_income_name = getTroopAttributes.income_specialist_name
    t3_income_power = getTroopAttributes.income_specialist_power
    t3_income_cost = getTroopAttributes.income_specialist_cost  
    untrained_name = getTroopAttributes.untrained_name  
    untrained_power = getTroopAttributes.untrained_power
    untrained_cost = getTroopAttributes.untrained_cost
    troopAttributes = {
            't1_attack_name': t1_attack_name,
            't1_attack_power': t1_attack_power,
            't1_attack_cost' : t1_attack_cost,
            't2_attack_name' : t2_attack_name,
            't2_attack_power' : t2_attack_power,
            't2_attack_cost' : t2_attack_cost,
            't3_attack_name' : t3_attack_name,
            't3_attack_power' : t3_attack_power,
            't3_attack_cost' : t3_attack_cost,
            't1_defence_name' : t1_defence_name,
            't1_defence_power' : t1_defence_power,
            't1_defence_cost' : t1_defence_cost,
            't2_defence_name' : t2_defence_name,
            't2_defence_power' : t2_defence_power,
            't2_defence_cost' : t2_defence_cost,
            't3_defence_name' : t3_defence_name,
            't3_defence_power' : t3_defence_power,
            't3_defence_cost' : t3_defence_cost,
            't1_intel_name' : t1_intel_name,
            't1_intel_power' : t1_intel_power,
            't1_intel_cost' : t1_intel_cost,
            't2_intel_name' : t2_intel_name,
            't2_intel_power' : t2_intel_power,
            't2_intel_cost' : t2_intel_cost,
            't3_intel_name' : t3_intel_name,
            't3_intel_power' : t3_intel_power,
            't3_intel_cost' : t3_intel_cost,
            't3_income_name' : t3_income_name,
            't3_income_power' : t3_income_power,
            't3_income_cost' : t3_income_cost,
            'untrained_name' : untrained_name,
            'untrained_power' : untrained_power,
            'untrained_cost' : untrained_cost,
        }    
    return troopAttributes
    
def getTroopNumbers(request):
    profile = UserProfile.objects.get(user=request.user)
    try:
        troops_object = Troops.objects.get(user_profile=profile)
        troopNumbers = {
        # Render Troop Count
        't1_attack' : troops_object.weak_attack_troops,        
        't2_attack' :  troops_object.strong_attack_troops,
        't3_attack' : troops_object.elite_attack_troops,
        't1_defence' : troops_object.weak_defence_troops,
        't2_defence' : troops_object.strong_defence_troops,
        't3_defence' : troops_object.elite_defence_troops,
        't1_intel' : troops_object.weak_intel_troops,
        't2_intel' : troops_object.strong_intel_troops,
        't3_intel' : troops_object.elite_intel_troops,
        't3_income' : troops_object.income_specialists,
        'untrained' : troops_object.untrained_units,
        }
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
        troopNumbers = {
        # Render Troop Count
        't1_attack' : troops_object.weak_attack_troops,        
        't2_attack' :  troops_object.strong_attack_troops,
        't3_attack' : troops_object.elite_attack_troops,
        't1_defence' : troops_object.weak_defence_troops,
        't2_defence' : troops_object.strong_defence_troops,
        't3_defence' : troops_object.elite_defence_troops,
        't1_intel' : troops_object.weak_intel_troops,
        't2_intel' : troops_object.strong_intel_troops,
        't3_intel' : troops_object.elite_intel_troops,
        't3_income' : troops_object.income_specialists,
        'untrained' : troops_object.untrained_units,
        }
    return troopNumbers
       







def renderMilitary(request):    
    troopAttributes = getTroopAttributes(request)
    troopNumbers = getTroopNumbers(request)
    #print(troopAttributes)
    #print(troopAttributes['t1_attack_name'])
    #print(troopAttributes.t1_attack_name)
    context = {'troopNumbers': troopNumbers, 'troopAttributes': troopAttributes}
    return render(request, 'military/military.html', context)



