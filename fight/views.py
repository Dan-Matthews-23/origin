from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from user_account.models import UserProfile
from player_power.models import PlayerPower
from military.models import Troops
from production.models import Production
from military.views import calculate_total_troops
from django.db.models import Sum
import random
from random import choice
from django.conf import settings
from reports.models import IntelLog
from django.contrib import messages



def check_intelligence(request, player_id):
    #higher_intel = False
    
    #Get User Profiles
    target_profile = UserProfile.objects.get(id=player_id)
    user_profile = UserProfile.objects.get(user=request.user)

    #Get Player Power
    target_intel = PlayerPower.objects.get(user_profile=target_profile)
    user_intel = PlayerPower.objects.get(user_profile=user_profile)    
   
    #print(f"Target intel is {target_intel.intel} and user intel is {user_intel.intel}")

    if user_intel.intel >= target_intel.intel:    
        higher_intel = True
    else:
        higher_intel = False
    
    return higher_intel










def fight(request):
    unknown = "Unknown"
    players = []
    player_data = {}
    profile = UserProfile.objects.get(user=request.user)
    get_user_power = PlayerPower.objects.get(user_profile=profile)

    for player in UserProfile.objects.all():#, Troops.objects.all():
        try:
            
            get_player_troops = Troops.objects.get(user_profile=player)
            get_player_power = PlayerPower.objects.get(user_profile=player)
            get_player_production = Production.objects.get(user_profile=player)

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
            players.append(player_data)  # Append data to the players list
            print(player_data)
        except PlayerPower.DoesNotExist:
            print("Not found")
    context = {'players': players}  # Pass the entire list to the context
    return render(request, 'fight/fight.html', context)







def player_info(request, player_id):
    unknown = "Unknown"
    player = UserProfile.objects.get(id=player_id)    
    get_player_troops = Troops.objects.get(user_profile=player)
    get_player_power = PlayerPower.objects.get(user_profile=player)
    get_player_production = Production.objects.get(user_profile=player)
    
    get_intel_status = check_intelligence(request, player_id)
    #print(get_intel_status)

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
    num_true = int(true_bias * 10)  # Assuming a scale of 10 (adjust as needed)
    num_false = 10 - num_true
    boolean_options = [True] * num_true + [False] * num_false
    return choice(boolean_options)






def spy(request, player_id):
    success = False
    player = UserProfile.objects.get(id=player_id)
    user = UserProfile.objects.get(user=request.user)

    get_user_intel_troops = Troops.objects.get(user_profile=user)
    get_player_intel_troops = Troops.objects.get(user_profile=player)

    get_player_power = PlayerPower.objects.get(user_profile=player)

    get_user_intel = PlayerPower.objects.get(user_profile=user)
    get_player_intel = PlayerPower.objects.get(user_profile=player)

    #If user intel is 50% or higher than target
    fifty_percent_higher_player = ((get_player_intel.intel/100)*50)+get_player_intel.intel
    twenty_five_percent_higher_player = ((get_player_intel.intel/100)*25)+get_player_intel.intel

    #If user intel is 50% or lower than target
    fifty_percent_lower_player = get_player_intel.intel - ((get_player_intel.intel/100)*50)  
    twenty_five_percent_lower_player = get_player_intel.intel - ((get_player_intel.intel/100)*25)

    print(f"User intel is {get_user_intel.intel}. Target intel is {get_player_intel.intel}. That means target intel 50% lower is expected to be 1000, and 25% lower is expected to be 1500. Actual results are: 50%: {fifty_percent_lower_player}, 25%: {twenty_five_percent_lower_player}")

    if get_user_intel.intel >= fifty_percent_higher_player:
        success = True
        result = "Overwhelming Victory"
        attacker_loss_weak = (settings.BASE_INTEL_LOSS_OVERWHELMING * get_user_intel_troops.weak_intel_troops)
        attacker_loss_strong = (settings.BASE_INTEL_LOSS_OVERWHELMING * get_user_intel_troops.strong_intel_troops)
        attacker_loss_elite = (settings.BASE_INTEL_LOSS_OVERWHELMING * get_user_intel_troops.elite_intel_troops)
        defender_loss_weak = (settings.BASE_INTEL_LOSS_OVERWHELMING * get_player_intel_troops.weak_intel_troops)
        defender_loss_strong = (settings.BASE_INTEL_LOSS_OVERWHELMING * get_player_intel_troops.strong_intel_troops)
        defender_loss_elite = (settings.BASE_INTEL_LOSS_OVERWHELMING * get_player_intel_troops.elite_intel_troops)
    
    elif get_user_intel.intel < fifty_percent_higher_player and get_user_intel.intel > twenty_five_percent_higher_player:
        true_bias = settings.TRUE_BIAS_TWENTY_FIVE_PERCENT
        success = biased_random_bool(true_bias)
        result = "Clear Victory"        
        attacker_loss_weak = (settings.BASE_INTEL_LOSS_CLEAR * get_user_intel_troops.weak_intel_troops)
        attacker_loss_strong = (settings.BASE_INTEL_LOSS_CLEAR * get_user_intel_troops.strong_intel_troops)
        attacker_loss_elite = (settings.BASE_INTEL_LOSS_CLEAR * get_user_intel_troops.elite_intel_troops)
        defender_loss_weak = (settings.BASE_INTEL_LOSS_CLEAR * get_player_intel_troops.weak_intel_troops)
        defender_loss_strong = (settings.BASE_INTEL_LOSS_CLEAR * get_player_intel_troops.strong_intel_troops)
        defender_loss_elite = (settings.BASE_INTEL_LOSS_CLEAR * get_player_intel_troops.elite_intel_troops)
      
    elif get_user_intel.intel > get_player_intel.intel and get_user_intel.intel < twenty_five_percent_higher_player:
        true_bias = settings.TRUE_BIAS_LESS_TWENTY_FIVE_PERCENT
        success = biased_random_bool(true_bias)
        result = "Victory"        
        attacker_loss_weak = (settings.BASE_INTEL_LOSS_VICTORY * get_user_intel_troops.weak_intel_troops)
        attacker_loss_strong = (settings.BASE_INTEL_LOSS_VICTORY * get_user_intel_troops.strong_intel_troops)
        attacker_loss_elite = (settings.BASE_INTEL_LOSS_VICTORY * get_user_intel_troops.elite_intel_troops)

        defender_loss_weak = (settings.BASE_INTEL_LOSS_VICTORY * get_player_intel_troops.weak_intel_troops)
        defender_loss_strong = (settings.BASE_INTEL_LOSS_VICTORY * get_player_intel_troops.strong_intel_troops)
        defender_loss_elite = (settings.BASE_INTEL_LOSS_VICTORY * get_player_intel_troops.elite_intel_troops)

    elif get_user_intel.intel <= fifty_percent_lower_player:        
        success = False
        result = "Overwhelming Loss"
        attacker_loss_weak = (settings.BASE_INTEL_LOSS_DEFEAT_OVERWHELMING * get_user_intel_troops.weak_intel_troops)
        attacker_loss_strong = (settings.BASE_INTEL_LOSS_DEFEAT_OVERWHELMING * get_user_intel_troops.strong_intel_troops)
        attacker_loss_elite = (settings.BASE_INTEL_LOSS_DEFEAT_OVERWHELMING * get_user_intel_troops.elite_intel_troops)

        defender_loss_weak = (settings.BASE_INTEL_LOSS_DEFEAT_OVERWHELMING * get_player_intel_troops.weak_intel_troops)
        defender_loss_strong = (settings.BASE_INTEL_LOSS_DEFEAT_OVERWHELMING * get_player_intel_troops.strong_intel_troops)
        defender_loss_elite = (settings.BASE_INTEL_LOSS_DEFEAT_OVERWHELMING * get_player_intel_troops.elite_intel_troops)

    elif get_user_intel.intel > fifty_percent_lower_player and get_user_intel.intel < twenty_five_percent_lower_player:
        success = False
        result = "Clear Loss"
        attacker_loss_weak = (settings.BASE_INTEL_LOSS_DEFEAT_CLEAR * get_user_intel_troops.weak_intel_troops)
        attacker_loss_strong = (settings.BASE_INTEL_LOSS_DEFEAT_CLEAR * get_user_intel_troops.strong_intel_troops)
        attacker_loss_elite = (settings.BASE_INTEL_LOSS_DEFEAT_CLEAR * get_user_intel_troops.elite_intel_troops)
        defender_loss_weak = (settings.BASE_INTEL_LOSS_DEFEAT_CLEAR * get_player_intel_troops.weak_intel_troops)
        defender_loss_strong = (settings.BASE_INTEL_LOSS_DEFEAT_CLEAR * get_player_intel_troops.strong_intel_troops)
        defender_loss_elite = (settings.BASE_INTEL_LOSS_DEFEAT_CLEAR * get_player_intel_troops.elite_intel_troops)
    
    elif get_user_intel.intel < get_player_intel.intel and get_user_intel.intel > twenty_five_percent_lower_player:
        success = False
        result = "Loss"
        attacker_loss_weak = (settings.BASE_INTEL_LOSS_DEFEAT_LOSS * get_user_intel_troops.weak_intel_troops)
        attacker_loss_strong = (settings.BASE_INTEL_LOSS_DEFEAT_LOSS * get_user_intel_troops.strong_intel_troops)
        attacker_loss_elite = (settings.BASE_INTEL_LOSS_DEFEAT_LOSS * get_user_intel_troops.elite_intel_troops)
        defender_loss_weak = (settings.BASE_INTEL_LOSS_DEFEAT_LOSS * get_player_intel_troops.weak_intel_troops)
        defender_loss_strong = (settings.BASE_INTEL_LOSS_DEFEAT_LOSS * get_player_intel_troops.strong_intel_troops)
        defender_loss_elite = (settings.BASE_INTEL_LOSS_DEFEAT_LOSS * get_player_intel_troops.elite_intel_troops)        
    else:
        messages.error(request, f"The calculations did not work. Actual user intel is {get_user_intel.intel} and target actual is {get_player_intel.intel}. Expected was 1500 and 2000. The expected fifty_lower was 1000. Actual is {fifty_percent_lower_player}. The expected 25_lower was 1500. Actual is {twenty_five_percent_lower_player}.")
        return redirect(request.META.get('HTTP_REFERER'))    
    if success == False:       
        create_log = IntelLog.objects.create(
            result=result,
            defender_user_profile=player,
            defender_intel=get_player_intel.intel,
            defender_troops=0,
            defender_technologies=0,
            defender_bonus=0,
            attacker_user_profile=user,
            attacker_intel=get_user_intel.intel,
            attacker_troops=0,
            attacker_technologies=0,
            attacker_bonus=0,
            attacker_weak_intel_troops_loss = attacker_loss_weak,
            attacker_strong_intel_troops_loss =  attacker_loss_strong,
            attacker_elite_intel_troops_loss = attacker_loss_elite,
            defender_defence_power = 0,
            defender_attack_power = 0,
            defender_intel_power = 0,
            defender_income_power = 0,
            defender_weak_attack_troops = 0,
            defender_strong_attack_troops = 0,
            defender_elite_attack_troops = 0,
            defender_weak_defence_troops = 0,
            defender_strong_defence_troops = 0,
            defender_elite_defence_troops = 0,
            defender_weak_intel_troops = 0,
            defender_strong_intel_troops = 0,
            defender_elite_intel_troops = 0,
            defender_income_specialists = 0,
            defender_untrained_units = 0,
                ) 
    elif success == True:
        print("True")        
        """create_log = IntelLog.objects.create(
            result=result,
            defender_user_profile=player,
            defender_intel=get_player_intel.intel,
            defender_troops=0,
            defender_technologies=0,
            defender_bonus=0,
            attacker_user_profile=user,
            attacker_intel=get_user_intel.intel,
            attacker_troops=0,
            attacker_technologies=0,
            attacker_bonus=0,
            attacker_weak_intel_troops_loss = attacker_loss_weak,
            attacker_strong_intel_troops_loss =  attacker_loss_strong,
            attacker_elite_intel_troops_loss = attacker_loss_elite,
            defender_defence_power = get_player_power.attack,
            defender_attack_power = get_player_power.defence,
            defender_intel_power = get_player_power.intel,
            defender_income_power = get_player_power.income,
            defender_weak_attack_troops = get_player_intel_troops.weak_attack_troops,
            defender_strong_attack_troops = get_player_intel_troops.strong_attack_troops,
            defender_elite_attack_troops = get_player_intel_troops.elite_attack_troops,
            defender_weak_defence_troops = get_player_intel_troops.weak_defence_troops,
            defender_strong_defence_troops = get_player_intel_troops.strong_defence_troops,
            defender_elite_defence_troops = get_player_intel_troops.elite_defence_troops,
            defender_weak_intel_troops = get_player_intel_troops.weak_intel_troops,
            defender_strong_intel_troops = get_player_intel_troops.strong_intel_troops,
            defender_elite_intel_troops = get_player_intel_troops.elite_intel_troops,
            defender_income_specialists = get_player_intel_troops.income_specialists,
            defender_untrained_units = get_player_intel_troops.untrained_units,
                )"""
        
    get_user_intel_troops.weak_intel_troops = (get_user_intel_troops.weak_intel_troops - attacker_loss_weak)
    get_user_intel_troops.strong_intel_troops = (get_user_intel_troops.strong_intel_troops - attacker_loss_strong)
    get_user_intel_troops.elite_intel_troops = (get_user_intel_troops.elite_intel_troops - attacker_loss_elite)
    get_user_intel_troops.save()     
    
    get_player_intel_troops.weak_intel_troops = (get_player_intel_troops.weak_intel_troops - defender_loss_weak)
    get_player_intel_troops.strong_intel_troops = (get_player_intel_troops.strong_intel_troops - defender_loss_strong)
    get_player_intel_troops.elite_intel_troops = (get_player_intel_troops.elite_intel_troops - defender_loss_elite)
    get_player_intel_troops.save()  

    
    return redirect('reports')



    
           












