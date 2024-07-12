from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from military.models import Troops

from user_account.models import UserProfile
from user_account.forms import UserProfileForm
from django.contrib import messages
from django.conf import settings
from faction_data.models import TroopAttributes
from production.models import Production
from player_power.views import calculate_attack, calculate_defence, calculate_intel, calculate_income
from player_power.models import PlayerPower


# Create your views here.

def calculate_attack_rank(request):
    for player in UserProfile.objects.all():       
        player_power = PlayerPower.objects.get(user_profile=player)       
        
        troops = Troops.objects.get(user_profile=player)
        total_attack_power = (
        troops.weak_attack_troops * TroopAttributes.objects.get().attack_tier_one_power +
        troops.strong_attack_troops * TroopAttributes.objects.get().attack_tier_two_power +
        troops.elite_attack_troops * TroopAttributes.objects.get().attack_tier_three_power
  )
       
        update_attack = PlayerPower.objects.get(user_profile=player)
        update_attack.attack = total_attack_power
        update_attack.save()
       
        all_players = PlayerPower.objects.all().order_by('-attack')
        update_attack.attack_rank = all_players.filter(attack__gt=update_attack.attack).count() + 1   
        update_attack.attack = total_attack_power
        update_attack.save()
       
        
    return update_attack


def calculate_defence_rank(request):
    for player in UserProfile.objects.all():       
        player_power = PlayerPower.objects.get(user_profile=player)       
        
        troops = Troops.objects.get(user_profile=player)
        total_defence_power = (
        troops.weak_defence_troops * TroopAttributes.objects.get().defence_tier_one_power +
        troops.strong_defence_troops * TroopAttributes.objects.get().defence_tier_two_power +
        troops.elite_defence_troops * TroopAttributes.objects.get().defence_tier_three_power
  )
       
        update_defence = PlayerPower.objects.get(user_profile=player)
        update_defence.defence = total_defence_power
        update_defence.save()
       
        all_players = PlayerPower.objects.all().order_by('-defence')
        update_defence.defence_rank = all_players.filter(defence__gt=update_defence.defence).count() + 1   
        update_defence.defence = total_defence_power
        update_defence.save()
        
        
    return update_defence


def initiate_turn_event(request):
    updated_attack = calculate_attack_rank(request)
    updated_defence = calculate_defence_rank(request)
    
    if updated_attack and updated_defence:
        message = "Turn Calculated"
    else:
        message = "Error in calculating turn"
    
    context = {
        'message': message,
    }
    print(message)
   
    return render(request, 'home/overview.html', context)


            

