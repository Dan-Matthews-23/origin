from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from game_settings.views import get_user, get_player, get_diplomacy

def diplomacy(request):    
    return render(request, 'diplomacy/diplomacy.html')


def make_ally(request, player_id):
    user = get_user(request)
    target = get_player(request, player_id)
    diplomacy_object = get_diplomacy(request, user, player_id)
    try:
        diplomacy_object.relation = "Ally"
        diplomacy_object.save()
        return redirect(request.META.get('HTTP_REFERER'))
    except diplomacy_object.DoesNotExist:
        messages.error("There was an error when setting relation to ally")
        return redirect(request.META.get('HTTP_REFERER'))


def make_enemy(request, player_id):
    user = get_user(request)
    target = get_player(request, player_id)
    diplomacy_object = get_diplomacy(request, user, player_id)
    try:
        diplomacy_object.relation = "Enemy"
        diplomacy_object.save()
        return redirect(request.META.get('HTTP_REFERER'))
    except diplomacy_object.DoesNotExist:
        messages.error("There was an error when setting relation to ally")
        return redirect(request.META.get('HTTP_REFERER'))
