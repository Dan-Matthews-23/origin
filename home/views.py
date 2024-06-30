from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from user_account.models import UserProfile
from player_power.models import PlayerPower
from military.models import Troops
from production.models import Production


def home(request):
    context = { }    
    return render(request, 'home/index.html', context)




def create_player_power_default(request):
    profile = UserProfile.objects.get(user=request.user)       
    try:
        getPlayerPower = PlayerPower.objects.get(user_profile=profile)
    except PlayerPower.DoesNotExist:
        create_power = PlayerPower.objects.create(
            user_profile=profile,
            attack=0,
            defence=0,
            intel=0,
            income=0,
            attack_rank=0,
            defence_rank=0,
            income_rank=0,
            overall_rank=0,
        )
        getPlayerPower = PlayerPower.objects.get(user_profile=profile)
    return getPlayerPower
    

def create_production_default(request):
    profile = UserProfile.objects.get(user=request.user)    
    try:
        production_object = Production.objects.get(user_profile=profile)
    except Production.DoesNotExist:       
        production_object = Production.objects.create(
            user_profile=profile,
            pop_growth=10,
            knowledge_points=10,
            income=10
        )
        production_object = Production.objects.get(user_profile=profile)
    return production_object
    

def create_troops_default(request):
    profile = UserProfile.objects.get(user=request.user)  
    try:
        troops_object = Troops.objects.get(user_profile=profile)
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
        troops_object = Troops.objects.get(user_profile=profile)
    return troops_object
   





@login_required
def overview(request):
    profile = UserProfile.objects.get(user=request.user)
    #create_player_power_default() 
    getPlayerPower = create_player_power_default(request)
    troops_object = create_troops_default(request)
    production_object = create_production_default(request)
    
    
    
    """try:
        getPlayerPower = PlayerPower.objects.get(user_profile=profile)
    except PlayerPower.DoesNotExist:
        create_power = PlayerPower.objects.create(
            user_profile=profile,
            attack=0,
            defence=0,
            intel=0,
            income=0,
            attack_rank=0,
            defence_rank=0,
            income_rank=0,
            overall_rank=0,
        )
        getPlayerPower = PlayerPower.objects.get(user_profile=profile) 
    """





    context = {
        'render_attack' : getPlayerPower.attack,
        'render_attack_rank': getPlayerPower.attack_rank,
        'render_defence' : getPlayerPower.defence,
        'render_defence_rank': getPlayerPower.defence_rank,
        'render_intel' : getPlayerPower.intel,
        'render_intel_rank': getPlayerPower.intel_rank,
        'render_income' : getPlayerPower.income,
        'render_income_rank': getPlayerPower.income_rank,
        }

    return render(request, 'home/overview.html', context)







