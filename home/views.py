from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from user_account.models import UserProfile
from player_power.models import PlayerPower


def home(request):
    context = { }    
    return render(request, 'home/index.html', context)


@login_required
def overview(request):
    profile = UserProfile.objects.get(user=request.user)    
    getPlayerPower = PlayerPower.objects.get(user_profile=profile)
    
    context = {
        'render_attack' : getPlayerPower.attack,
        'render_defence' : getPlayerPower.defence,
        'render_intel' : getPlayerPower.intel,
        'render_income' : getPlayerPower.income,
    }

    return render(request, 'home/overview.html', context)







