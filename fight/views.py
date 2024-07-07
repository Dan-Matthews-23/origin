from django.shortcuts import render
from django.contrib.auth.models import User
from user_account.models import UserProfile
from player_power.models import PlayerPower
from military.models import Troops
from production.models import Production



def fight(request):
    players = []
    player_data = {}
    profile = UserProfile.objects.get(user=request.user)
    get_user_power = PlayerPower.objects.get(user_profile=profile)

    for player in UserProfile.objects.all():#, Troops.objects.all():
        try:
            get_player_troops = Troops.objects.get(user_profile=player)
            get_player_power = PlayerPower.objects.get(user_profile=player)
            get_player_production = Production.objects.get(user_profile=player)

            if get_user_power.intel >= get_player_power.intel:
                player_troops = get_player_troops.weak_attack_troops
                player_data_crystal_balance =  f"{get_player_production.data_crystal_balance:,}"
            else:
                player_troops = "???"
                player_data_crystal_balance = "???"           
            
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
    player = UserProfile.objects.get(id=player_id)
    
    get_player_troops = Troops.objects.get(user_profile=player)
    get_player_power = PlayerPower.objects.get(user_profile=player)
    get_player_production = Production.objects.get(user_profile=player)

    player_info = {
        'get_player_troops': get_player_troops.weak_attack_troops,
        'get_player_power': get_player_power.attack,
        'get_player_production': get_player_production.data_crystal_balance,        
    }

    context = {'player_info': player_info}

    return render(request, 'fight/player_info.html', context)











