from django.shortcuts import render
from django.contrib.auth.models import User
from user_account.models import UserProfile
from player_power.models import PlayerPower



def fight(request):
    players = []
    for player in UserProfile.objects.all():
        try:
            get_players = PlayerPower.objects.get(user_profile=player)
            player_data = {
                
                'username': player.user,
                'faction': player.faction,
                'attack': get_players.attack,
            }
            players.append(player_data)  # Append data to the players list
            print(player_data)
        except PlayerPower.DoesNotExist:
            print("Not found")
    context = {'players': players}  # Pass the entire list to the context
    return render(request, 'fight/fight.html', context)











