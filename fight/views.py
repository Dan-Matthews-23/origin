import sys
import random
import inspect
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import resolve, Resolver404
from django.conf import settings
from django.contrib import messages
from user_account.models import UserProfile
from player_power.models import PlayerPower
from player_power.views import calculate_defence, calculate_attack
from military.models import Troops
from production.models import Production
from military.views import calculate_total_troops
from random import choice
from reports.models import IntelLog, AttackLog
from error_log.models import ErrorLog
from user_account.views import get_user, get_player
from military.views import return_troops
from player_power.views import return_power
from production.views import production_object, get_data_crystal_balance


def get_app_name(request):
    current_frame = inspect.currentframe()
    caller_frame = current_frame.f_back
    function_name = caller_frame.f_code.co_name
    app_name = caller_frame.f_globals['__name__'].split('.')[0]
    return app_name


def get_function_name(request):
    current_frame = inspect.currentframe()
    caller_frame = current_frame.f_back
    function_name = caller_frame.f_code.co_name    
    return function_name


def create_log(request, app_name, function_name, error):
    create_log = ErrorLog.objects.create(
    user=user,
    app = app_name,
    function = function_name,
    error=error
    )
    user_error=error
    return user_error







def check_intelligence(request, player_id):   
    target_profile = UserProfile.objects.get(id=player_id)
    user_profile = UserProfile.objects.get(user=request.user)    
    target_intel = PlayerPower.objects.get(user_profile=target_profile)
    user_intel = PlayerPower.objects.get(user_profile=user_profile)    
    if user_intel.intel >= target_intel.intel:    
        higher_intel = True
    else:
        higher_intel = False
    
    return higher_intel


def fight(request):
    unknown = "Unknown"
    players = []
    player_data = {}
    profile = get_user(request)
    get_user_power = return_power(request, profile)    
    for player in UserProfile.objects.all():
        try:            
            get_player_troops = return_troops(request, player)            
            get_player_power = return_power(request, player)
            get_player_production = production_object(request, player)
            player_id =  player.id
            get_intel_status = check_intelligence(request, player_id)
            if get_intel_status == True:
                player_troops = get_player_troops.weak_attack_troops
                player_data_crystal_balance =  f"{get_player_production.data_crystal_balance:,}"
            else:
                player_troops = unknown
                player_data_crystal_balance = unknown            
            player_data = {                
                'username': player.user,
                'id': player.id,
                'faction': player.faction,
                'attack': get_player_power.attack,
                'intel': get_player_power.intel,
                'army_size': player_troops,
                'data_crystal_balance': player_data_crystal_balance,
            }
            players.append(player_data)  
            #print(player_data)
        except PlayerPower.DoesNotExist:
            print("Not found")
    context = {'players': players} 
    return render(request, 'fight/fight.html', context)


def player_info(request, player_id):
    unknown = "Unknown"
    player = UserProfile.objects.get(id=player_id)    
    get_player_troops = return_troops(request, player)            
    get_player_power = return_power(request, player)
    get_player_production = production_object(request, player)  
    get_intel_status = check_intelligence(request, player_id)
    if get_intel_status == True:
        get_total_army = calculate_total_troops(request, player_id)    
        target_troops = {
            'weak_attack_troops': get_player_troops.weak_attack_troops, 
            'strong_attack_troops': get_player_troops.strong_attack_troops,
            'elite_attack_troops': get_player_troops.elite_attack_troops,
            'weak_defence_troops': get_player_troops.weak_defence_troops,
            'strong_defence_troops': get_player_troops.strong_defence_troops,
            'elite_defence_troops': get_player_troops.elite_defence_troops,
            'weak_intel_troops':get_player_troops.weak_intel_troops,
            'strong_intel_troops': get_player_troops.strong_intel_troops,
            'elite_intel_troops': get_player_troops.elite_intel_troops,
            'income_specialists':get_player_troops.income_specialists,
            'untrained_units':get_player_troops.untrained_units,
            'total_army': get_total_army,
            'data_crystal_balance': f"{get_player_production.data_crystal_balance:,}", 
            }
    else:
        target_troops = {
            'weak_attack_troops': unknown, 
            'strong_attack_troops': unknown,
            'elite_attack_troops': unknown,
            'weak_defence_troops': unknown,
            'strong_defence_troops': unknown,
            'elite_defence_troops': unknown,
            'weak_intel_troops': unknown,
            'strong_intel_troops': unknown,
            'elite_intel_troops': unknown,
            'income_specialists': unknown,
            'untrained_units': unknown,
            'get_player_troops': unknown,
            'total_army': unknown,
            'data_crystal_balance': unknown, 
        }    
    player_info = {
        'target_name': player.user,
        'target_faction': player.faction,
        'player_id': player.id,
    }
    context = {'player_info': player_info, 'target_troops': target_troops}
    return render(request, 'fight/player_info.html', context)


def biased_random_bool(true_bias):
    num_true = int(true_bias * 10) 
    num_false = 10 - num_true
    boolean_options = [True] * num_true + [False] * num_false
    return choice(boolean_options)

def calculate_fifty_percent(request, player_id, weighting, attack_type):
    player = get_player(request, player_id)
    player_power = return_power(request, player)

    if attack_type == "Intel":
        if weighting == "Higher":
            calculate_fifty_percent = ((player_power.intel/100)*50)+player_power.intel            
            return calculate_fifty_percent
        elif weighting == "Lower":
            calculate_fifty_percent = player_power.intel - ((player_power.intel/100)*50)
            return calculate_fifty_percent
    elif attack_type =="Attack":   
        if weighting == "Higher":
            calculate_fifty_percent = ((player_power.defence/100)*50)+player_power.defence            
            return calculate_fifty_percent
        elif weighting == "Lower":
            calculate_fifty_percent = player_power.defence - ((player_power.defence/100)*50)
            return calculate_fifty_percent
        



def calculate_twenty_five_percent(request, player_id, weighting, attack_type):
    player = get_player(request, player_id)
    player_power = return_power(request, player)

    if attack_type =="Intel":    
        if weighting == "Higher":
            calculate_twenty_five_percent = ((player_power.intel/100)*25)+player_power.intel
            return calculate_twenty_five_percent
        elif weighting == "Lower":
            calculate_twenty_five_percent = player_power.intel - ((player_power.intel/100)*25)
            return calculate_twenty_five_percent
    elif attack_type == "Attack":
        if weighting == "Higher":
            calculate_twenty_five_percent = ((player_power.defence/100)*25)+player_power.defence
            return calculate_twenty_five_percent
        elif weighting == "Lower":
            calculate_twenty_five_percent = player_power.defence - ((player_power.defence/100)*25)
            return calculate_twenty_five_percent


def calculate_overwhelming_victory(request, player_id, attack_type):
    player = get_player(request, player_id)
    user = get_user(request)

    get_user_troops = return_troops(request, user)
    get_target_troops = return_troops(request, player)

    get_user_power = return_power(request, user)
    get_target_power = return_power(request, player)

    get_production_object = production_object(request, player)


    success = True
    attacker_result = "Overwhelming Victory"
    defender_result = "Overwhelming Defeat"

    if attack_type == "Intel":

        attacker_loss_weak = (settings.ATTACKER_LOSS_FOR_OVERWHELMING_SUCCESS_ATTACK * get_user_troops.weak_intel_troops)
        attacker_loss_strong = (settings.ATTACKER_LOSS_FOR_OVERWHELMING_SUCCESS_ATTACK * get_user_troops.strong_intel_troops)
        attacker_loss_elite = (settings.ATTACKER_LOSS_FOR_OVERWHELMING_SUCCESS_ATTACK * get_user_troops.elite_intel_troops)

        defender_loss_weak = (settings.DEFENDER_LOSS_FOR_OVERWHELMING_SUCCESS_ATTACK * get_target_troops.weak_intel_troops)
        defender_loss_strong = (settings.DEFENDER_LOSS_FOR_OVERWHELMING_SUCCESS_ATTACK * get_target_troops.strong_intel_troops)
        defender_loss_elite = (settings.DEFENDER_LOSS_FOR_OVERWHELMING_SUCCESS_ATTACK * get_target_troops.elite_intel_troops)

        results = {
            'get_target_power': get_target_power,
            'get_user_power': get_user_power,
            'success': success,
            'attacker_result': attacker_result,
            'defender_result': defender_result,
            #'data_crystal_gain': data_crystal_gain,
            'attacker_loss_weak': attacker_loss_weak,
            'attacker_loss_strong': attacker_loss_strong,
            'attacker_loss_elite': attacker_loss_elite,
            'defender_loss_weak': defender_loss_weak,
            'defender_loss_strong': defender_loss_strong,
            'defender_loss_elite': defender_loss_elite,
        }
        return results
    
    elif attack_type == "Attack":
        

        success = True
        attacker_result = "Overwhelming Victory"
        defender_result = "Overwhelming Defeat"

        data_crystal_gain = ((get_production_object.data_crystal_balance/100)*settings.INCOME_GAIN_FOR_OVERWHELMING_SUCCESS_ATTACK)              

        attacker_loss_weak = (settings.ATTACKER_LOSS_FOR_OVERWHELMING_SUCCESS_ATTACK * get_user_troops.weak_attack_troops)
        attacker_loss_strong = (settings.ATTACKER_LOSS_FOR_OVERWHELMING_SUCCESS_ATTACK * get_user_troops.strong_attack_troops)
        attacker_loss_elite = (settings.ATTACKER_LOSS_FOR_OVERWHELMING_SUCCESS_ATTACK * get_user_troops.elite_attack_troops)

        defender_loss_weak = (settings.DEFENDER_LOSS_FOR_OVERWHELMING_SUCCESS_ATTACK * get_target_troops.weak_defence_troops)
        defender_loss_strong = (settings.DEFENDER_LOSS_FOR_OVERWHELMING_SUCCESS_ATTACK * get_target_troops.strong_defence_troops)
        defender_loss_elite = (settings.DEFENDER_LOSS_FOR_OVERWHELMING_SUCCESS_ATTACK * get_target_troops.elite_defence_troops)

        results = {
            'get_target_power': get_target_power,
            'get_user_power': get_user_power,
            'success': success,
            'attacker_result': attacker_result,
            'defender_result': defender_result,
            'data_crystal_gain': data_crystal_gain,
            'attacker_loss_weak': attacker_loss_weak,
            'attacker_loss_strong': attacker_loss_strong,
            'attacker_loss_elite': attacker_loss_elite,
            'defender_loss_weak': defender_loss_weak,
            'defender_loss_strong': defender_loss_strong,
            'defender_loss_elite': defender_loss_elite,
        }
        return results

        

def calculate_clear_victory(request, player_id, attack_type):
    player = get_player(request, player_id)
    user = get_user(request)

    get_user_troops = return_troops(request, user)
    get_target_troops = return_troops(request, player)

    get_user_power = return_power(request, user)
    get_target_power = return_power(request, player)

    get_production_object = production_object(request, player)
    success = True
    attacker_result = "Clear Victory"
    defender_result = "Clear Defeat"

    if attack_type == "Intel":       

        attacker_loss_weak = (settings.ATTACKER_LOSS_FOR_CLEAR_SUCCESS_ATTACK * get_user_troops.weak_intel_troops)
        attacker_loss_strong = (settings.ATTACKER_LOSS_FOR_CLEAR_SUCCESS_ATTACK * get_user_troops.strong_intel_troops)
        attacker_loss_elite = (settings.ATTACKER_LOSS_FOR_CLEAR_SUCCESS_ATTACK * get_user_troops.elite_intel_troops)

        defender_loss_weak = (settings.DEFENDER_LOSS_FOR_CLEAR_SUCCESS_ATTACK * get_target_troops.weak_intel_troops)
        defender_loss_strong = (settings.DEFENDER_LOSS_FOR_CLEAR_SUCCESS_ATTACK * get_target_troops.strong_intel_troops)
        defender_loss_elite = (settings.DEFENDER_LOSS_FOR_CLEAR_SUCCESS_ATTACK * get_target_troops.elite_intel_troops)

        results = {
            'get_target_power': get_target_power,
            'get_user_power': get_user_power,
            'success': success,
            'attacker_result': attacker_result,
            'defender_result': defender_result,
            #'data_crystal_gain': data_crystal_gain,
            'attacker_loss_weak': attacker_loss_weak,
            'attacker_loss_strong': attacker_loss_strong,
            'attacker_loss_elite': attacker_loss_elite,
            'defender_loss_weak': defender_loss_weak,
            'defender_loss_strong': defender_loss_strong,
            'defender_loss_elite': defender_loss_elite,
        }
        return results

        
    
    elif attack_type == "Attack":
        player = get_player(request, player_id)
        user = get_user(request)

        get_user_troops = return_troops(request, user)
        get_target_troops = return_troops(request, player)

        get_user_power = return_power(request, user)
        get_target_power = return_power(request, player)

        get_production_object = production_object(request, player)

        true_bias = settings.TRUE_BIAS_TWENTY_FIVE_PERCENT
        success = biased_random_bool(true_bias)
        attacker_result = "Clear Victory"
        defender_result = "Clear Defeat"

        data_crystal_gain = ((get_production_object.data_crystal_balance/100)*settings.INCOME_GAIN_FOR_CLEAR_SUCCESS_ATTACK)

        attacker_loss_weak = (settings.ATTACKER_LOSS_FOR_CLEAR_SUCCESS_ATTACK * get_user_troops.weak_attack_troops)
        attacker_loss_strong = (settings.ATTACKER_LOSS_FOR_CLEAR_SUCCESS_ATTACK * get_user_troops.strong_attack_troops)
        attacker_loss_elite = (settings.ATTACKER_LOSS_FOR_CLEAR_SUCCESS_ATTACK * get_user_troops.elite_attack_troops)

        defender_loss_weak = (settings.DEFENDER_LOSS_FOR_CLEAR_SUCCESS_ATTACK * get_target_troops.weak_defence_troops)
        defender_loss_strong = (settings.DEFENDER_LOSS_FOR_CLEAR_SUCCESS_ATTACK * get_target_troops.strong_defence_troops)
        defender_loss_elite = (settings.DEFENDER_LOSS_FOR_CLEAR_SUCCESS_ATTACK * get_target_troops.elite_defence_troops)
        results = {
            'get_target_power': get_target_power,
            'get_user_power': get_user_power,
            'success': success,
            'attacker_result': attacker_result,
            'defender_result': defender_result,
            'data_crystal_gain': data_crystal_gain,
            'attacker_loss_weak': attacker_loss_weak,
            'attacker_loss_strong': attacker_loss_strong,
            'attacker_loss_elite': attacker_loss_elite,
            'defender_loss_weak': defender_loss_weak,
            'defender_loss_strong': defender_loss_strong,
            'defender_loss_elite': defender_loss_elite,
        }
        return results

        

def calculate_narrow_victory(request, player_id, attack_type):
    player = get_player(request, player_id)
    user = get_user(request)

    get_user_troops = return_troops(request, user)
    get_target_troops = return_troops(request, player)

    get_user_power = return_power(request, user)
    get_target_power = return_power(request, player)

    get_production_object = production_object(request, player)
    success = True
    attacker_result = "Victory"
    defender_result = "Defeat"

    if attack_type == "Intel":
        

        attacker_loss_weak = (settings.ATTACKER_LOSS_FOR_NARROW_SUCCESS_ATTACK * get_user_troops.weak_intel_troops)
        attacker_loss_strong = (settings.ATTACKER_LOSS_FOR_NARROW_SUCCESS_ATTACK * get_user_troops.strong_intel_troops)
        attacker_loss_elite = (settings.ATTACKER_LOSS_FOR_NARROW_SUCCESS_ATTACK * get_user_troops.elite_intel_troops)

        defender_loss_weak = (settings.DEFENDER_LOSS_FOR_NARROW_SUCCESS_ATTACK * get_target_troops.weak_intel_troops)
        defender_loss_strong = (settings.DEFENDER_LOSS_FOR_NARROW_SUCCESS_ATTACK * get_target_troops.strong_intel_troops)
        defender_loss_elite = (settings.DEFENDER_LOSS_FOR_NARROW_SUCCESS_ATTACK * get_target_troops.elite_intel_troops)

        results = {
            'get_target_power': get_target_power,
            'get_user_power': get_user_power,
            'success': success,
            'attacker_result': attacker_result,
            'defender_result': defender_result,
            #'data_crystal_gain': data_crystal_gain,
            'attacker_loss_weak': attacker_loss_weak,
            'attacker_loss_strong': attacker_loss_strong,
            'attacker_loss_elite': attacker_loss_elite,
            'defender_loss_weak': defender_loss_weak,
            'defender_loss_strong': defender_loss_strong,
            'defender_loss_elite': defender_loss_elite,
        }
        return results
    
    elif attack_type == "Attack":      

        true_bias = settings.TRUE_BIAS_LESS_TWENTY_FIVE_PERCENT
        success = biased_random_bool(true_bias)
        attacker_result = "Victory"
        defender_result = "Defeat"

        data_crystal_gain = ((get_production_object.data_crystal_balance/100)*settings.INCOME_GAIN_FOR_NARROW_SUCCESS_ATTACK)

        attacker_loss_weak = (settings.ATTACKER_LOSS_FOR_NARROW_SUCCESS_ATTACK * get_user_troops.weak_attack_troops)
        attacker_loss_strong = (settings.ATTACKER_LOSS_FOR_NARROW_SUCCESS_ATTACK * get_user_troops.strong_attack_troops)
        attacker_loss_elite = (settings.ATTACKER_LOSS_FOR_NARROW_SUCCESS_ATTACK * get_user_troops.elite_attack_troops)

        defender_loss_weak = (settings.DEFENDER_LOSS_FOR_NARROW_SUCCESS_ATTACK * get_target_troops.weak_defence_troops)
        defender_loss_strong = (settings.DEFENDER_LOSS_FOR_NARROW_SUCCESS_ATTACK * get_target_troops.strong_defence_troops)
        defender_loss_elite = (settings.DEFENDER_LOSS_FOR_NARROW_SUCCESS_ATTACK * get_target_troops.elite_defence_troops)

        results = {
            'get_target_power': get_target_power,
            'get_user_power': get_user_power,
            'success': success,
            'attacker_result': attacker_result,
            'defender_result': defender_result,
            'data_crystal_gain': data_crystal_gain,
            'attacker_loss_weak': attacker_loss_weak,
            'attacker_loss_strong': attacker_loss_strong,
            'attacker_loss_elite': attacker_loss_elite,
            'defender_loss_weak': defender_loss_weak,
            'defender_loss_strong': defender_loss_strong,
            'defender_loss_elite': defender_loss_elite,
        }
        return results


def calculate_overwhelming_defeat(request, player_id, attack_type):
    player = get_player(request, player_id)
    user = get_user(request)

    get_user_troops = return_troops(request, user)
    get_target_troops = return_troops(request, player)

    get_user_power = return_power(request, user)
    get_target_power = return_power(request, player)

    success = True
    attacker_result = "Overwhelming Defeat"
    defender_result = "Overwhelming Victory"

    if attack_type == "Intel":        

        attacker_loss_weak = (settings.ATTACKER_LOSS_FOR_OVERWHELMING_FAILURE_ATTACK * get_user_troops.weak_intel_troops)
        attacker_loss_strong = (settings.ATTACKER_LOSS_FOR_OVERWHELMING_FAILURE_ATTACK * get_user_troops.strong_intel_troops)
        attacker_loss_elite = (settings.ATTACKER_LOSS_FOR_OVERWHELMING_FAILURE_ATTACK * get_user_troops.elite_intel_troops)

        defender_loss_weak = (settings.DEFENDER_LOSS_FOR_OVERWHELMING_FAILURE_ATTACK * get_target_troops.weak_intel_troops)
        defender_loss_strong = (settings.DEFENDER_LOSS_FOR_OVERWHELMING_FAILURE_ATTACK * get_target_troops.strong_intel_troops)
        defender_loss_elite = (settings.DEFENDER_LOSS_FOR_OVERWHELMING_FAILURE_ATTACK * get_target_troops.elite_intel_troops)

        results = {
            'get_target_power': get_target_power,
            'get_user_power': get_user_power,
            'success': success,
            'attacker_result': attacker_result,
            'defender_result': defender_result,
            #'data_crystal_gain': data_crystal_gain,
            'attacker_loss_weak': attacker_loss_weak,
            'attacker_loss_strong': attacker_loss_strong,
            'attacker_loss_elite': attacker_loss_elite,
            'defender_loss_weak': defender_loss_weak,
            'defender_loss_strong': defender_loss_strong,
            'defender_loss_elite': defender_loss_elite,
        }
        return results
    
    elif attack_type == "Attack":
        

        success = False
        attacker_result = "Overwhelming Defeat"
        defender_result = "Overwhelming Victory"
        data_crystal_gain = 0
        attacker_loss_weak = (settings.ATTACKER_LOSS_FOR_OVERWHELMING_FAILURE_ATTACK * get_user_troops.weak_attack_troops)
        attacker_loss_strong = (settings.ATTACKER_LOSS_FOR_OVERWHELMING_FAILURE_ATTACK * get_user_troops.strong_attack_troops)
        attacker_loss_elite = (settings.ATTACKER_LOSS_FOR_OVERWHELMING_FAILURE_ATTACK * get_user_troops.elite_attack_troops)

        defender_loss_weak = (settings.DEFENDER_LOSS_FOR_OVERWHELMING_FAILURE_ATTACK * get_target_troops.weak_defence_troops)
        defender_loss_strong = (settings.DEFENDER_LOSS_FOR_OVERWHELMING_FAILURE_ATTACK * get_target_troops.strong_defence_troops)
        defender_loss_elite = (settings.DEFENDER_LOSS_FOR_OVERWHELMING_FAILURE_ATTACK * get_target_troops.elite_defence_troops)

          
        results = {
            'get_target_power': get_target_power,
            'get_user_power': get_user_power,
            'success': success,
            'attacker_result': attacker_result,
            'defender_result': defender_result,
            'data_crystal_gain': data_crystal_gain,
            'attacker_loss_weak': attacker_loss_weak,
            'attacker_loss_strong': attacker_loss_strong,
            'attacker_loss_elite': attacker_loss_elite,
            'defender_loss_weak': defender_loss_weak,
            'defender_loss_strong': defender_loss_strong,
            'defender_loss_elite': defender_loss_elite,
        }
        return results


def return_attacker_result(results):
    attacker_result = results['attacker_result']
    return attacker_result


def return_defender_result(results):
    defender_result = results['defender_result']
    return defender_result
    

def calculate_clear_defeat(request, player_id, attack_type):
    player = get_player(request, player_id)
    user = get_user(request)

    get_user_troops = return_troops(request, user)
    get_target_troops = return_troops(request, player)

    get_user_power = return_power(request, user)
    get_target_power = return_power(request, player)

    get_production_object = production_object(request, player)
    success = True
    attacker_result = "Clear Defeat"
    defender_result = "Clear Victory"

    if attack_type == "Intel":
        

        attacker_loss_weak = (settings.ATTACKER_LOSS_FOR_CLEAR_FAILURE_ATTACK * get_user_troops.weak_intel_troops)
        attacker_loss_strong = (settings.ATTACKER_LOSS_FOR_CLEAR_FAILURE_ATTACK * get_user_troops.strong_intel_troops)
        attacker_loss_elite = (settings.ATTACKER_LOSS_FOR_CLEAR_FAILURE_ATTACK * get_user_troops.elite_intel_troops)

        defender_loss_weak = (settings.DEFENDER_LOSS_FOR_CLEAR_FAILURE_ATTACK * get_target_troops.weak_intel_troops)
        defender_loss_strong = (settings.DEFENDER_LOSS_FOR_CLEAR_FAILURE_ATTACK * get_target_troops.strong_intel_troops)
        defender_loss_elite = (settings.DEFENDER_LOSS_FOR_CLEAR_FAILURE_ATTACK * get_target_troops.elite_intel_troops)

        results = {
            'get_target_power': get_target_power,
            'get_user_power': get_user_power,
            'success': success,
            'attacker_result': attacker_result,
            'defender_result': defender_result,
            #'data_crystal_gain': data_crystal_gain,
            'attacker_loss_weak': attacker_loss_weak,
            'attacker_loss_strong': attacker_loss_strong,
            'attacker_loss_elite': attacker_loss_elite,
            'defender_loss_weak': defender_loss_weak,
            'defender_loss_strong': defender_loss_strong,
            'defender_loss_elite': defender_loss_elite,
        }
        return results
    
    elif attack_type == "Attack":      

        success = False
        attacker_result = "Clear Defeat"
        defender_result = "Clear Victory"
        data_crystal_gain = 0

        attacker_loss_weak = (settings.ATTACKER_LOSS_FOR_CLEAR_FAILURE_ATTACK * get_user_troops.weak_attack_troops)
        attacker_loss_strong = (settings.ATTACKER_LOSS_FOR_CLEAR_FAILURE_ATTACK * get_user_troops.strong_attack_troops)
        attacker_loss_elite = (settings.ATTACKER_LOSS_FOR_CLEAR_FAILURE_ATTACK * get_user_troops.elite_attack_troops)

        defender_loss_weak = (settings.DEFENDER_LOSS_FOR_CLEAR_FAILURE_ATTACK * get_target_troops.weak_defence_troops)
        defender_loss_strong = (settings.DEFENDER_LOSS_FOR_CLEAR_FAILURE_ATTACK * get_target_troops.strong_defence_troops)
        defender_loss_elite = (settings.DEFENDER_LOSS_FOR_CLEAR_FAILURE_ATTACK * get_target_troops.elite_defence_troops)

        results = {
            'get_target_power': get_target_power,
            'get_user_power': get_user_power,
            'success': success,
            'attacker_result': attacker_result,
            'defender_result': defender_result,
            'data_crystal_gain': data_crystal_gain,
            'attacker_loss_weak': attacker_loss_weak,
            'attacker_loss_strong': attacker_loss_strong,
            'attacker_loss_elite': attacker_loss_elite,
            'defender_loss_weak': defender_loss_weak,
            'defender_loss_strong': defender_loss_strong,
            'defender_loss_elite': defender_loss_elite,
        }
        return results
    

def calculate_narrow_defeat(request, player_id, attack_type):
    player = get_player(request, player_id)
    user = get_user(request)

    get_user_troops = return_troops(request, user)
    get_target_troops = return_troops(request, player)

    get_user_power = return_power(request, user)
    get_target_power = return_power(request, player)

    get_production_object = production_object(request, player)

    success = True
    attacker_result = "Defeat"
    defender_result = "Victory"

    if attack_type == "Intel":      

        attacker_loss_weak = (settings.ATTACKER_LOSS_FOR_NARROW_FAILURE_ATTACK * get_user_troops.weak_intel_troops)
        attacker_loss_strong = (settings.ATTACKER_LOSS_FOR_NARROW_FAILURE_ATTACK * get_user_troops.strong_intel_troops)
        attacker_loss_elite = (settings.ATTACKER_LOSS_FOR_NARROW_FAILURE_ATTACK * get_user_troops.elite_intel_troops)

        defender_loss_weak = (settings.DEFENDER_LOSS_FOR_NARROW_FAILURE_ATTACK * get_target_troops.weak_intel_troops)
        defender_loss_strong = (settings.DEFENDER_LOSS_FOR_NARROW_FAILURE_ATTACK * get_target_troops.strong_intel_troops)
        defender_loss_elite = (settings.DEFENDER_LOSS_FOR_NARROW_FAILURE_ATTACK * get_target_troops.elite_intel_troops)

        results = {
            'get_target_power': get_target_power,
            'get_user_power': get_user_power,
            'success': success,
            'attacker_result': attacker_result,
            'defender_result': defender_result,
            #'data_crystal_gain': data_crystal_gain,
            'attacker_loss_weak': attacker_loss_weak,
            'attacker_loss_strong': attacker_loss_strong,
            'attacker_loss_elite': attacker_loss_elite,
            'defender_loss_weak': defender_loss_weak,
            'defender_loss_strong': defender_loss_strong,
            'defender_loss_elite': defender_loss_elite,
        }
        return results
    
    elif attack_type == "Attack":     

        success = False
        attacker_result = "Defeat"
        defender_result = "Victory"
        data_crystal_gain = 0

        attacker_loss_weak = (settings.ATTACKER_LOSS_FOR_NARROW_FAILURE_ATTACK * get_user_troops.weak_attack_troops)
        attacker_loss_strong = (settings.ATTACKER_LOSS_FOR_NARROW_FAILURE_ATTACK * get_user_troops.strong_attack_troops)
        attacker_loss_elite = (settings.ATTACKER_LOSS_FOR_NARROW_FAILURE_ATTACK * get_user_troops.elite_attack_troops)

        defender_loss_weak = (settings.DEFENDER_LOSS_FOR_NARROW_FAILURE_ATTACK * get_target_troops.weak_defence_troops)
        defender_loss_strong = (settings.DEFENDER_LOSS_FOR_NARROW_FAILURE_ATTACK * get_target_troops.strong_defence_troops)
        defender_loss_elite = (settings.DEFENDER_LOSS_FOR_NARROW_FAILURE_ATTACK * get_target_troops.elite_defence_troops) 

        results = {
            'get_target_power': get_target_power,
            'get_user_power': get_user_power,
            'success': success,
            'attacker_result': attacker_result,
            'defender_result': defender_result,
            'data_crystal_gain': data_crystal_gain,
            'attacker_loss_weak': attacker_loss_weak,
            'attacker_loss_strong': attacker_loss_strong,
            'attacker_loss_elite': attacker_loss_elite,
            'defender_loss_weak': defender_loss_weak,
            'defender_loss_strong': defender_loss_strong,
            'defender_loss_elite': defender_loss_elite,
        }
        return results
    









def spy(request, player_id):
    success = False
    attack_type = "Intel"
    player = get_player(request, player_id)
    user = get_user(request)
    attacker_troops = return_troops(request, user)
    defender_troops = return_troops(request, player)     

    user_data_crystal_balance = get_data_crystal_balance(request, user)
    player_data_crystal_balance = get_data_crystal_balance(request, player)    
    
    get_user_power = return_power(request, user)
    get_player_power = return_power(request, player)

   
    fifty_percent_higher = calculate_fifty_percent(request, player_id, "Higher", attack_type)
    twenty_five_percent_higher = calculate_twenty_five_percent(request, player_id, "Higher", attack_type)

    fifty_percent_lower = calculate_fifty_percent(request, player_id, "Lower", attack_type)
    twenty_five_percent_lower = calculate_twenty_five_percent(request, player_id, "Lower", attack_type)    

    if get_user_power.intel >= fifty_percent_higher:
        results = calculate_overwhelming_victory(request, player_id, attack_type)
        attacker_result = return_attacker_result(results)
        defender_result = return_defender_result(results)

    
    elif get_user_power.intel < fifty_percent_higher and get_user_power.intel > twenty_five_percent_higher:
        results = calculate_clear_victory(request, player_id, attack_type)
        attacker_result = return_attacker_result(results)
        defender_result = return_defender_result(results)
      
    elif get_user_power.intel > get_player_power.intel and get_user_power.intel < twenty_five_percent_higher:
        results = calculate_narrow_victory(request, player_id, attack_type)
        attacker_result = return_attacker_result(results)
        defender_result = return_defender_result(results)
        
    elif get_user_power.intel <= fifty_percent_lower:
        results = calculate_overwhelming_defeat(request, player_id, attack_type)
        attacker_result = return_attacker_result(results)
        defender_result = return_defender_result(results)
        
    elif get_user_power.intel > fifty_percent_lower and get_user_power.intel <= twenty_five_percent_lower:
        results = calculate_clear_defeat(request, player_id, attack_type)        
        attacker_result = return_attacker_result(results)
        defender_result = return_defender_result(results)
    
    elif get_user_power.intel <= get_player_power.intel and get_user_power.intel > twenty_five_percent_lower:
        results = calculate_narrow_defeat(request, player_id, attack_type)
        attacker_result = return_attacker_result(results)
        defender_result = return_defender_result(results)
               
    else:
        error = "User intel did not match any parameters in spy function."       
        app_name = get_app_name(request)
        function_name = get_function_name(request)
        create_log = create_log(request, app_name, function_name, error)
        messages.error(request, user_error)       
        return redirect(request.META.get('HTTP_REFERER'))    
    
    if success == False:       
            create_attack_log = IntelLog.objects.create(
                result=attacker_result,
                defender_user_profile=player, 
                defender_intel=get_player_power.intel,               
                defender_weak_intel_troops_loss=results['defender_loss_weak'],
                defender_strong_intel_troops_loss=results['defender_loss_strong'],
                defender_elite_intel_troops_loss=results['defender_loss_elite'],
                attacker_user_profile=user,                   
                attacker_weak_intel_troops_loss=results['attacker_loss_weak'],
                attacker_strong_intel_troops_loss=results['attacker_loss_strong'],
                attacker_elite_intel_troops_loss=results['attacker_loss_elite'],
                defender_defence_power=get_player_power.defence,
                defender_attack_power=get_player_power.attack,
                defender_income_power=get_player_power.income,
                defender_weak_attack_troops=defender_troops.weak_attack_troops,
                defender_strong_attack_troops=defender_troops.strong_attack_troops,
                defender_elite_attack_troops=defender_troops.elite_attack_troops,
                defender_weak_defence_troops=defender_troops.weak_defence_troops,
                defender_strong_defence_troops=defender_troops.strong_defence_troops,
                defender_elite_defence_troops=defender_troops.elite_defence_troops,
                defender_weak_intel_troops=defender_troops.weak_intel_troops,
                defender_strong_intel_troops=defender_troops.strong_intel_troops,
                defender_elite_intel_troops=defender_troops.elite_intel_troops,
                defender_income_specialists=defender_troops.income_specialists,
                defender_untrained_units=defender_troops.untrained_units,         
                             
            
            
            )
           
    elif success == True:
        #print("True")        
        create_attack_log = IntelLog.objects.create(
            result=attacker_result,
                defender_user_profile=player, 
                defender_intel=get_player_power.intel,               
                defender_weak_intel_troops_loss=results['defender_loss_weak'],
                defender_strong_intel_troops_loss=results['defender_loss_strong'],
                defender_elite_intel_troops_loss=results['defender_loss_elite'],
                attacker_user_profile=user,                   
                attacker_weak_intel_troops_loss=results['attacker_loss_weak'],
                attacker_strong_intel_troops_loss=results['attacker_loss_strong'],
                attacker_elite_intel_troops_loss=results['attacker_loss_elite'],
                defender_defence_power=get_player_power.defence,
                defender_attack_power=get_player_power.attack,
                defender_income_power=get_player_power.income,
                defender_weak_attack_troops=defender_troops.weak_attack_troops,
                defender_strong_attack_troops=defender_troops.strong_attack_troops,
                defender_elite_attack_troops=defender_troops.elite_attack_troops,
                defender_weak_defence_troops=defender_troops.weak_defence_troops,
                defender_strong_defence_troops=defender_troops.strong_defence_troops,
                defender_elite_defence_troops=defender_troops.elite_defence_troops,
                defender_weak_intel_troops=defender_troops.weak_intel_troops,
                defender_strong_intel_troops=defender_troops.strong_intel_troops,
                defender_elite_intel_troops=defender_troops.elite_intel_troops,
                defender_income_specialists=defender_troops.income_specialists,
                defender_untrained_units=defender_troops.untrained_units,
            
           
                )
            
        
           
                
        
    attacker_troops.weak_intel_troops = (attacker_troops.weak_intel_troops - results['attacker_loss_weak'])
    attacker_troops.strong_intel_troops = (attacker_troops.strong_intel_troops - results['attacker_loss_strong'])
    attacker_troops.elite_intel_troops = (attacker_troops.elite_intel_troops - results['attacker_loss_elite'])
    #print(f"Attacker Loss is {attacker_loss_weak}, {attacker_loss_strong} and {attacker_loss_elite}")
    attacker_troops.save()
    update_attacker_attack = calculate_attack(request, player_id)
    #print(f"New attacker attack power is {update_attacker_attack}")
            
    
    defender_troops.weak_intel_troops = (defender_troops.weak_intel_troops - results['defender_loss_weak'])
    defender_troops.strong_intel_troops = (defender_troops.strong_intel_troops - results['defender_loss_strong'])
    defender_troops.elite_intel_troops = (defender_troops.elite_intel_troops - results['defender_loss_elite'])    
    defender_troops.save()

    update_defender_defence = calculate_defence(request, player_id)         
    return redirect('intel_reports')


def attack(request, player_id):
    success = False
    attack_type = "Attack"
    player = get_player(request, player_id)
    user = get_user(request)
    attacker_troops = return_troops(request, user)
    defender_troops = return_troops(request, player)     

    user_data_crystal_balance = get_data_crystal_balance(request, user)
    player_data_crystal_balance = get_data_crystal_balance(request, player)
    
    get_player_power = PlayerPower.objects.get(user_profile=player)
    get_user_attack = return_power(request, user)
    get_player_defence = return_power(request, player)

   
    fifty_percent_higher = calculate_fifty_percent(request, player_id, "Higher", attack_type)
    twenty_five_percent_higher = calculate_twenty_five_percent(request, player_id, "Higher", attack_type)

    fifty_percent_lower = calculate_fifty_percent(request, player_id, "Lower", attack_type)
    twenty_five_percent_lower = calculate_twenty_five_percent(request, player_id, "Lower", attack_type)    

    if get_user_attack.attack >= fifty_percent_higher:
        results = calculate_overwhelming_victory(request, player_id, attack_type)
        attacker_result = return_attacker_result(results)
        defender_result = return_defender_result(results)

    
    elif get_user_attack.attack < fifty_percent_higher and get_user_attack.attack > twenty_five_percent_higher:
        results = calculate_clear_victory(request, player_id, attack_type)
        attacker_result = return_attacker_result(results)
        defender_result = return_defender_result(results)
      
    elif get_user_attack.attack > get_player_defence.defence and get_user_attack.attack < twenty_five_percent_higher:
        results = calculate_narrow_victory(request, player_id, attack_type)
        attacker_result = return_attacker_result(results)
        defender_result = return_defender_result(results)
        
    elif get_user_attack.attack <= fifty_percent_lower:
        results = calculate_overwhelming_defeat(request, player_id, attack_type)
        attacker_result = return_attacker_result(results)
        defender_result = return_defender_result(results)
        
    elif get_user_attack.attack > fifty_percent_lower and get_user_attack.attack <= twenty_five_percent_lower:
        results = calculate_clear_defeat(request, player_id, attack_type)        
        attacker_result = return_attacker_result(results)
        defender_result = return_defender_result(results)
    
    elif get_user_attack.attack <= get_player_defence.defence and get_user_attack.attack > twenty_five_percent_lower:
        results = calculate_narrow_defeat(request, player_id, attack_type)
        attacker_result = return_attacker_result(results)
        defender_result = return_defender_result(results)
               
    else:
        error = "User intel did not match any parameters in spy function."       
        app_name = get_app_name(request)
        function_name = get_function_name(request)
        create_log = create_log(request, app_name, function_name, error)
        messages.error(request, user_error)       
        return redirect(request.META.get('HTTP_REFERER'))    
    
    if success == False:       
            create_attack_log = AttackLog.objects.create(
            result=attacker_result,
            defender_user_profile=player,                 
            attacker_user_profile=user,
            attacker_attack_snap  = get_user_attack.attack,
            defender_defence_snap = get_player_defence.defence,        
            attacker_t1_loss = results['attacker_loss_weak'],
            attacker_t2_loss =  results['attacker_loss_strong'],
            attacker_t3_loss = results['attacker_loss_elite'],
            defender_t1_loss = results['defender_loss_weak'],
            defender_t2_loss = results['defender_loss_strong'],
            defender_t3_loss = results['defender_loss_elite'],            
            attacker_t1_count = attacker_troops.weak_attack_troops,
            attacker_t2_count = attacker_troops.strong_attack_troops,
            attacker_t3_count = attacker_troops.elite_attack_troops,           
            defender_t1_count = defender_troops.weak_defence_troops,
            defender_t2_count = defender_troops.strong_defence_troops,
            defender_t3_count = defender_troops.elite_defence_troops,
            data_crystal_gain = results['data_crystal_gain'],
            )
           
    elif success == True:
        #print("True")        
        create_attack_log = AttackLog.objects.create(
            result=attacker_result,
            defender_user_profile=player,                 
            attacker_user_profile=user,
            attacker_attack_snap  = get_user_attack.attack,
            defender_defence_snap = get_player_defence.defence,        
            attacker_t1_loss = attacker_loss_weak,
            attacker_t2_loss =  attacker_loss_strong,
            attacker_t3_loss = attacker_loss_elite,
            defender_t1_loss = defender_loss_weak,
            defender_t2_loss = defender_loss_strong,
            defender_t3_loss = defender_loss_elite,            
            attacker_t1_count = attacker_troops.weak_attack_troops,
            attacker_t2_count = attacker_troops.strong_attack_troops,
            attacker_t3_count = attacker_troops.elite_attack_troops,           
            defender_t1_count = defender_troops.weak_defence_troops,
            defender_t2_count = defender_troops.strong_defence_troops,
            defender_t3_count = defender_troops.elite_defence_troops,
            data_crystal_gain = data_crystal_gain,
           
                )
            
        
           
                
        
    attacker_troops.weak_attack_troops = (attacker_troops.weak_attack_troops - results['attacker_loss_weak'])
    attacker_troops.strong_attack_troops = (attacker_troops.strong_attack_troops - results['attacker_loss_strong'])
    attacker_troops.elite_attack_troops = (attacker_troops.elite_attack_troops - results['attacker_loss_elite'])
    #print(f"Attacker Loss is {attacker_loss_weak}, {attacker_loss_strong} and {attacker_loss_elite}")
    attacker_troops.save()
    update_attacker_attack = calculate_attack(request, player_id)
    #print(f"New attacker attack power is {update_attacker_attack}")
            
    
    defender_troops.weak_defence_troops = (defender_troops.weak_defence_troops - results['defender_loss_weak'])
    defender_troops.strong_defence_troops = (defender_troops.strong_defence_troops - results['defender_loss_strong'])
    defender_troops.elite_defence_troops = (defender_troops.elite_defence_troops - results['defender_loss_elite'])
    #print(f"Defence Loss is {defender_loss_weak}, {defender_loss_strong} and {defender_loss_elite}")
    defender_troops.save()

    update_defender_defence = calculate_defence(request, player_id)
    #print(f"New defender defence power is {update_defender_defence}")

    calculate_data_crystal(request, results, player, "Loss")
    calculate_data_crystal(request, results, user, "Gain")
    

    #player_data_crystal_balance.data_crystal_balance = player_data_crystal_balance.data_crystal_balance - results['data_crystal_gain']
    #player_data_crystal_balance.save()

    #user_data_crystal_balance.data_crystal_balance  = user_data_crystal_balance.data_crystal_balance +  results['data_crystal_gain']
    #user_data_crystal_balance.save()

    #print(f"Defender loses {data_crystal_gain}")    
         
    return redirect('attack_reports')


def calculate_data_crystal(request, results, user, weighting):
    query = production_object(request, user)
    if weighting == "Loss":
        query.data_crystal_balance = query.data_crystal_balance - results['data_crystal_gain']
        query.save()
    elif weighting == "Gain":
        query.data_crystal_balance = query.data_crystal_balance + results['data_crystal_gain']
        query.save()



    
           












