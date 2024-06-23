from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from .models import Troops
from user_account.models import UserProfile
from user_account.forms import UserProfileForm
from django.contrib import messages
from django.conf import settings
from faction_data.models import TroopAttributes
from production.models import Production
from player_power.views import calculate_attack, calculate_defence, calculate_intel, calculate_income


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


def trainTroops(request):

    signal = True

    profile = UserProfile.objects.get(user=request.user)   
    production_object = Production.objects.get(user_profile=profile)

    t1_quantity_attack = int(request.POST.get('t1_attack'))
    t2_quantity_attack = int(request.POST.get('t2_attack'))
    t3_quantity_attack = int(request.POST.get('t3_attack'))
    t1_quantity_defence = int(request.POST.get('t1_defence'))
    t2_quantity_defence = int(request.POST.get('t2_defence'))
    t3_quantity_defence = int(request.POST.get('t3_defence'))
    t1_quantity_intel = int(request.POST.get('t1_intel'))
    t2_quantity_intel = int(request.POST.get('t2_intel'))
    t3_quantity_intel = int(request.POST.get('t3_intel'))
    t3_quantity_income = int(request.POST.get('t3_income'))

    troopAttributes = getTroopAttributes(request)
    troopNumbers = getTroopNumbers(request)

    data = {
    "attack": int(request.POST.get('t1_attack')) + int(request.POST.get('t2_attack')) + int(request.POST.get('t3_attack')),
    "defence": int(request.POST.get('t1_defence')) + int(request.POST.get('t2_defence')) + int(request.POST.get('t3_defence')),
    "intel": int(request.POST.get('t1_intel')) + int(request.POST.get('t2_intel')) + int(request.POST.get('t3_intel')),
    "income": int(request.POST.get('t3_income')),  # Assuming only one income value
    }
    # Accessing totals:
    attack_total = data["attack"]
    defence_total = data["defence"]
    intel_total = data["intel"]
    income_total = data["income"]

    if attack_total > troopNumbers['untrained']:
        messages.error(request, 'You do not have enough untrained units to train that many attack troops')
        signal = False        
        return redirect(request.META.get('HTTP_REFERER'))
        #print("You do not have enough untrained units to train that many attack troops")
    
    if defence_total > troopNumbers['untrained']:
        messages.error(request, 'You do not have enough untrained units to train that many defence troops')
        signal = False 
        return redirect(request.META.get('HTTP_REFERER'))
        #print("You do not have enough untrained units to train that many defence troops")
    
    if intel_total > troopNumbers['untrained']:
        messages.error(request, 'You do not have enough untrained units to train that many intel troops')
        signal = False 
        return redirect(request.META.get('HTTP_REFERER'))
        #print("You do not have enough untrained units to train that many defence troops")

    if income_total > troopNumbers['untrained']:
        messages.error(request, 'You do not have enough untrained units to train that many incoome troops')
        signal = False 
        return redirect(request.META.get('HTTP_REFERER'))
        #print("You do not have enough untrained units to train that many defence troops")
    
    
    t1_attack_cost = (troopAttributes['t1_attack_cost'] * t1_quantity_attack)
    t2_attack_cost = (troopAttributes['t2_attack_cost'] * t2_quantity_attack)
    t3_attack_cost = (troopAttributes['t3_attack_cost'] * t3_quantity_attack)

    t1_defence_cost = (troopAttributes['t1_defence_cost'] * t1_quantity_defence)
    t2_defence_cost = (troopAttributes['t2_defence_cost'] * t2_quantity_defence)
    t3_defence_cost = (troopAttributes['t3_defence_cost'] * t3_quantity_defence)

    t1_intel_cost = (troopAttributes['t1_intel_cost'] * t1_quantity_intel)
    t2_intel_cost = (troopAttributes['t2_intel_cost'] * t2_quantity_intel)
    t3_intel_cost = (troopAttributes['t3_intel_cost'] * t3_quantity_intel)

    t3_income_cost = (troopAttributes['t3_income_cost'] * t3_quantity_income)



    if production_object.data_crystal_balance < t1_attack_cost:
        messages.error(request, 'You do not have enough data crystals to train that many attack troops')
        signal = False 
        return redirect(request.META.get('HTTP_REFERER'))
    
    if production_object.data_crystal_balance < t2_attack_cost:
        messages.error(request, 'You do not have enough data crystals to train that many attack troops')
        signal = False 
        return redirect(request.META.get('HTTP_REFERER'))
    
    if production_object.data_crystal_balance < t3_attack_cost:
        messages.error(request, 'You do not have enough data crystals to train that many attack troops')
        signal = False 
        return redirect(request.META.get('HTTP_REFERER'))
    
    if production_object.data_crystal_balance < t1_defence_cost:
        messages.error(request, 'You do not have enough data crystals to train that many defence troops')
        signal = False 
        return redirect(request.META.get('HTTP_REFERER'))
    
    if production_object.data_crystal_balance < t2_defence_cost:
        messages.error(request, 'You do not have enough data crystals to train that many defence troops')
        signal = False 
        return redirect(request.META.get('HTTP_REFERER'))
    
    if production_object.data_crystal_balance < t3_defence_cost:
        messages.error(request, 'You do not have enough data crystals to train that many defence troops')
        signal = False 
        return redirect(request.META.get('HTTP_REFERER'))
    
    if production_object.data_crystal_balance < t1_intel_cost:
        messages.error(request, 'You do not have enough data crystals to train that many intel troops')
        signal = False 
        return redirect(request.META.get('HTTP_REFERER'))
    
    if production_object.data_crystal_balance < t2_intel_cost:
        messages.error(request, 'You do not have enough data crystals to train that many intel troops')
        signal = False 
        return redirect(request.META.get('HTTP_REFERER'))
    
    if production_object.data_crystal_balance < t3_intel_cost:
        messages.error(request, 'You do not have enough data crystals to train that many intel troops')
        signal = False 
        return redirect(request.META.get('HTTP_REFERER'))
    
    if production_object.data_crystal_balance < t3_income_cost:
        messages.error(request, 'You do not have enough data crystals to train that many income troops')
        signal = False 
        return redirect(request.META.get('HTTP_REFERER'))
    
    if signal == True:
        t1_attack_power = (troopAttributes['t1_attack_power'] * t1_quantity_attack)
        t2_attack_power = (troopAttributes['t2_attack_power'] * t2_quantity_attack)
        t3_attack_power = (troopAttributes['t3_attack_power'] * t3_quantity_attack)

        t1_defence_power = (troopAttributes['t1_defence_power'] * t1_quantity_defence)
        t2_defence_power = (troopAttributes['t2_defence_power'] * t2_quantity_defence)
        t3_defence_power = (troopAttributes['t3_defence_power'] * t3_quantity_defence)

        t1_intel_power = (troopAttributes['t1_intel_power'] * t1_quantity_intel)
        t2_intel_power = (troopAttributes['t2_intel_power'] * t2_quantity_intel)
        t3_intel_power = (troopAttributes['t3_intel_power'] * t3_quantity_intel)

        t3_income_power = (troopAttributes['t3_income_power'] * t3_quantity_income)


        print("Yes, you have enough money and untrained to do this")
        calculateAttack = calculate_attack(request)
        calculateDefence = calculate_defence(request)
        calculateIntel = calculate_intel(request)
        calculateIncome = calculate_income(request)
        print(calculateAttack)     
    return redirect('renderMilitary')



