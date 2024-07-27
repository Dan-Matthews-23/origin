from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from military.models import Troops
#from django.db.models import F, DenseRank
from django.core.exceptions import ObjectDoesNotExist

from user_account.models import UserProfile
from user_account.forms import UserProfileForm
from django.contrib import messages
from django.conf import settings
from faction_data.models import TroopAttributes
from production.models import Production
from player_power.models import PlayerPower
from game_settings.views import get_power
import logging
logger = logging.getLogger(__name__) 


def calculate_attack_rank(request):
    rank_list = []
    has_errors = False
    for player in UserProfile.objects.all():
        try:
            power = PlayerPower.objects.get(user_profile=player)
            get_attack = power.attack 
            rank_list.append({
                'player': player,
                'power': power,  
                'calculation': get_attack,
            })
        except PlayerPower.DoesNotExist:
            has_errors = True
            logger.error(f"Power object not found for user {player}")
        except django.db.utils.IntegrityError as e:
            has_errors = True
            logger.error(f"Database error updating Power object for {player}: {e}")  
    rank_list.sort(key=lambda x: x['calculation'], reverse=True)    
    for index, item in enumerate(rank_list, start=1):
        item['position'] = index
        item['power'].attack_rank = index
        item['power'].save()
    return has_errors


def calculate_defence_rank(request):
    rank_list = []
    has_errors = False
    for player in UserProfile.objects.all():
        try:
            power = PlayerPower.objects.get(user_profile=player)
            get_defence = power.defence 
            rank_list.append({
                'player': player,
                'power': power,  
                'calculation': get_defence,
            })
        except PlayerPower.DoesNotExist:
            has_errors = True
            logger.error(f"Power object not found for user {player}")
        except django.db.utils.IntegrityError as e:
            has_errors = True
            logger.error(f"Database error updating Power object for {player}: {e}")  
    rank_list.sort(key=lambda x: x['calculation'], reverse=True)    
    for index, item in enumerate(rank_list, start=1):
        item['position'] = index
        item['power'].defence_rank = index
        item['power'].save()
    return has_errors


def calculate_intel_rank(request):
    rank_list = []
    has_errors = False
    for player in UserProfile.objects.all():
        try:
            power = PlayerPower.objects.get(user_profile=player)
            get_intel = power.intel 
            rank_list.append({
                'player': player,
                'power': power,  
                'calculation': get_intel,
            })
        except PlayerPower.DoesNotExist:
            has_errors = True
            logger.error(f"Power object not found for user {player}")
        except django.db.utils.IntegrityError as e:
            has_errors = True
            logger.error(f"Database error updating Power object for {player}: {e}")  
    rank_list.sort(key=lambda x: x['calculation'], reverse=True)    
    for index, item in enumerate(rank_list, start=1):
        item['position'] = index
        item['power'].intel_rank = index
        item['power'].save()
    return has_errors


def calculate_income_rank(request):
    rank_list = []
    has_errors = False
    for player in UserProfile.objects.all():
        try:
            power = PlayerPower.objects.get(user_profile=player)
            get_income = power.income 
            rank_list.append({
                'player': player,
                'power': power,  
                'calculation': get_income,
            })
        except PlayerPower.DoesNotExist:
            has_errors = True
            logger.error(f"Power object not found for user {player}")
        except django.db.utils.IntegrityError as e:
            has_errors = True
            logger.error(f"Database error updating Power object for {player}: {e}")  
    rank_list.sort(key=lambda x: x['calculation'], reverse=True)    
    for index, item in enumerate(rank_list, start=1):
        item['position'] = index
        item['power'].income_rank = index
        item['power'].save()
    return has_errors


def calculate_production(request):
    has_errors = False
    for player in UserProfile.objects.all():
        try:
            production = Production.objects.get(user_profile=player)
            troops = Troops.objects.get(user_profile=player)
        except Production.DoesNotExist:
            has_errors = True
            logger.error(f"Production object not found for user {player}")
            continue  
        except Troops.DoesNotExist:
            has_errors = True
            logger.error(f"Troops object not found for user {player}")
            continue  
        except django.db.utils.IntegrityError as e:
            has_errors = True
            logger.error(f"Database error updating production and troops for user {player}: {e}")
        else:           
            production.data_crystal_balance += production.income
            production.knowledge_points += production.knowledge_points_growth
            troops.untrained_units += production.pop_growth
            try:
                production.save()
                troops.save()
            except Exception as e:
                has_errors = True
                logger.error(f"Error saving production and troops for user {player}: {e}")
    return has_errors


def calculate_total_rank(request):
    rank_list = []
    has_errors = False
    for player in UserProfile.objects.all():
        try:
            power = PlayerPower.objects.get(user_profile=player)
            calculate_overall = (power.attack_rank + power.defence_rank + power.intel_rank + power.income_rank)
            rank_list.append({
                'player': player,
                'power': power,  
                'calculation': calculate_overall,            })
        except PlayerPower.DoesNotExist:
            has_errors = True
            logger.error(f"Power object not found for user {player}")
        except django.db.utils.IntegrityError as e:
            has_errors = True
            logger.error(f"Database error updating Power object for {player}: {e}")   
    rank_list.sort(key=lambda x: x['calculation'])   
    for index, item in enumerate(rank_list, start=1):
        item['position'] = index
        item['power'].overall_rank = index
        item['power'].save()  
    return has_errors


def initiate_turn_event(request):
    update_attack = calculate_attack_rank(request)
    update_defence = calculate_defence_rank(request)
    update_intel = calculate_intel_rank(request)
    update_income = calculate_income_rank(request)
    update_production = calculate_production(request)
    update_total_rank = calculate_total_rank(request)
    error_messages = []    
    if update_attack == True:
        error_messages.append("Error calculating attack rank")    
    if update_defence == True:
        error_messages.append("Error calculating defence rank")    
    if update_production == True:
        error_messages.append("Error calculating production")
    if update_intel == True:
        error_messages.append("Error calculating intel")
    if update_income == True:
        error_messages.append("Error calculating income")
    if error_messages:
        message = "Turn calculation encountered errors:"
    else:
        message = "Turn Calculated Successfully"    
    context = {'message': message}   
    if error_messages:
        context['error_messages'] = error_messages   
    return render(request, 'home/overview.html', context)




