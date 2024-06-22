from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from .models import Troops
from user_account.models import UserProfile
from user_account.forms import UserProfileForm
from django.contrib import messages
from django.conf import settings

def military(request):
    profile = UserProfile.objects.get(user=request.user)
    try:
        troops_object = Troops.objects.get(user_profile=profile)
       
        # Render Troop Count
        weak_attack_troops = troops_object.weak_attack_troops        
        strong_attack_troops =  troops_object.strong_attack_troops
        elite_attack_troops = troops_object.elite_attack_troops
        weak_defence_troops = troops_object.weak_defence_troops
        strong_defence_troops = troops_object.strong_defence_troops
        elite_defence_troops = troops_object.elite_defence_troops
        weak_intel_troops = troops_object.weak_intel_troops
        strong_intel_troops = troops_object.strong_intel_troops
        elite_intel_troops = troops_object.elite_intel_troops
        income_specialists = troops_object.income_specialists
        untrained_units = troops_object.untrained_units    
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
        weak_attack_troops = troops_object.weak_attack_troops        
        strong_attack_troops =  troops_object.strong_attack_troops
        elite_attack_troops = troops_object.elite_attack_troops
        weak_defence_troops = troops_object.weak_defence_troops
        strong_defence_troops = troops_object.strong_defence_troops
        elite_defence_troops = troops_object.elite_defence_troops
        weak_intel_troops = troops_object.weak_intel_troops
        strong_intel_troops = troops_object.strong_intel_troops
        elite_intel_troops = troops_object.elite_intel_troops
        income_specialists = troops_object.income_specialists
        untrained_units = troops_object.untrained_units    
    context = {
        'weak_attack_troops' : weak_attack_troops,      
        'strong_attack_troops':  strong_attack_troops,
        'elite_attack_troops': elite_attack_troops,
        'weak_defence_troops': weak_defence_troops,
        'strong_defence_troops' : strong_defence_troops,
        'elite_defence_troops' : elite_defence_troops,
        'weak_intel_troops' : weak_intel_troops,
        'strong_intel_troops' : strong_intel_troops,
        'elite_intel_troops' : elite_intel_troops,
        'income_specialists' : income_specialists,
        'untrained_units' : untrained_units,
    }
    return render(request, 'military/military.html', context)


