from django.shortcuts import render
from django.contrib.auth.models import User
from user_account.models import UserProfile
from player_power.models import PlayerPower
from military.models import Troops
from production.models import Production
from military.views import calculate_total_troops
from django.db.models import Sum


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
        'get_player_power': get_player_power.attack,       
         
    }

    context = {'player_info': player_info, 'target_troops': target_troops}

    return render(request, 'fight/player_info.html', context)


    
           












