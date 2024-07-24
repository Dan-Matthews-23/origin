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
from player_power.views import calculate_attack, calculate_defence, calculate_intel, calculate_income
from player_power.models import PlayerPower

import logging

logger = logging.getLogger(__name__)  # Get logger for this module


# Create your views here.

def calculate_attack_rank(request):
    has_errors = False
    for player in UserProfile.objects.all():
        try:
            player_power = PlayerPower.objects.get(user_profile=player)
            troops = Troops.objects.get(user_profile=player)
        except PlayerPower.DoesNotExist:
            has_errors = True
            logger.error(f"PlayerPower object not found for user {player}")
            continue        
        except Troops.DoesNotExist:
            has_errors = True
            logger.error(f"Troops object not found for user {player}")
            continue
        except django.db.utils.IntegrityError as e:
            has_errors = True
            logger.error(f"Database error updating PlayerPower and troops for user {player}: {e}")        
        else:        
            total_attack_power = (
            troops.weak_attack_troops * TroopAttributes.objects.get().attack_tier_one_power +
            troops.strong_attack_troops * TroopAttributes.objects.get().attack_tier_two_power +
            troops.elite_attack_troops * TroopAttributes.objects.get().attack_tier_three_power
            )        
            update_attack = PlayerPower.objects.get(user_profile=player)
            update_attack.attack = total_attack_power
            try:
                update_attack.save()
            except Exception as e:
                has_errors = True
                logger.error(f"Error saving production and troops for user {player}: {e}")        
            all_players = PlayerPower.objects.all().order_by('-attack')
            update_attack.attack_rank = all_players.filter(attack__gt=update_attack.attack).count() + 1   
            update_attack.attack = total_attack_power
            try:
                update_attack.save()
            except Exception as e:
                has_errors = True
                logger.error(f"Error saving production and troops for user {player}: {e}")
    return has_errors




def calculate_defence_rank(request):
    has_errors = False
    for player in UserProfile.objects.all():
        try:
            player_power = PlayerPower.objects.get(user_profile=player)
            troops = Troops.objects.get(user_profile=player)
        except PlayerPower.DoesNotExist:
            has_errors = True
            logger.error(f"PlayerPower object not found for user {player}")
            continue        
        except Troops.DoesNotExist:
            has_errors = True
            logger.error(f"Troops object not found for user {player}")
            continue
        except django.db.utils.IntegrityError as e:
            has_errors = True
            logger.error(f"Database error updating PlayerPower and troops for user {player}: {e}")        
        else:        
            total_defence_power = (
            troops.weak_defence_troops * TroopAttributes.objects.get().defence_tier_one_power +
            troops.strong_defence_troops * TroopAttributes.objects.get().defence_tier_two_power +
            troops.elite_defence_troops * TroopAttributes.objects.get().defence_tier_three_power
            )        
            update_defence = PlayerPower.objects.get(user_profile=player)
            update_defence.defence = total_defence_power
            try:
                update_defence.save()
            except Exception as e:
                has_errors = True
                logger.error(f"Error saving production and troops for user {player}: {e}")        
            all_players = PlayerPower.objects.all().order_by('-defence')
            update_defence.defence_rank = all_players.filter(defence__gt=update_defence.defence).count() + 1   
            update_defence.defence = total_defence_power
            try:
                update_defence.save()
            except Exception as e:
                has_errors = True
                logger.error(f"Error saving production and troops for user {player}: {e}")
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
                'power': power,  # Store power object for later update
                'calculation': calculate_overall,
            })
        except PlayerPower.DoesNotExist:
            has_errors = True
            logger.error(f"Power object not found for user {player}")
        except django.db.utils.IntegrityError as e:
            has_errors = True
            logger.error(f"Database error updating Power object for {player}: {e}")

    # Sort the rank_list by calculation in ascending order
    rank_list.sort(key=lambda x: x['calculation'])

    # Assign positions and update overall_rank
    for index, item in enumerate(rank_list, start=1):
        item['position'] = index
        item['power'].overall_rank = index
        item['power'].save()  # Save the updated PlayerPower object

    return rank_list, has_errors










            
            
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           



def initiate_turn_event(request):
    update_attack = calculate_attack_rank(request)
    update_defence = calculate_defence_rank(request)
    update_production = calculate_production(request)
    update_total_rank = calculate_total_rank(request)
    error_messages = []    
    if update_attack == True:
        error_messages.append("Error calculating attack rank")    
    if update_defence == True:
        error_messages.append("Error calculating defence rank")    
    if update_production == True:
        error_messages.append("Error calculating production")    
    if error_messages:
        message = "Turn calculation encountered errors:"
    else:
        message = "Turn Calculated Successfully"    
    context = {'message': message}   
    if error_messages:
        context['error_messages'] = error_messages   
    return render(request, 'home/overview.html', context)


            

