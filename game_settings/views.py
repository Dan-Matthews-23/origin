from django.shortcuts import render

from faction_data.models import TroopAttributes
from military.views import Troops
from production.models import Production
from player_power.models import PlayerPower
from user_account.views import UserProfile

def get_user(request):
    user = UserProfile.objects.get(user=request.user)
    return user


def get_power(request, user):
    get_power = PlayerPower.objects.get(user_profile=user)
    return get_power


def get_player(request, player_id):
    player = UserProfile.objects.get(id=player_id)
    return player





def get_production(request, user):
    production_object = Production.objects.get(user_profile=user)
    return production_object


def get_troops(request, user):
    get_troops = Troops.objects.get(user_profile=user)
    return get_troops


def get_troop_attributes(request):
    query = TroopAttributes.objects.all()
    if query.exists():
        troop_attributes = query.first()
        details = {
            'attack_tier_one_name': troop_attributes.attack_tier_one_name,
            'attack_tier_one_power': troop_attributes.attack_tier_one_power,
            'attack_tier_one_cost': troop_attributes.attack_tier_one_cost,
            'attack_tier_two_name': troop_attributes.attack_tier_two_name,
            'attack_tier_two_power': troop_attributes.attack_tier_two_power,
            'attack_tier_two_cost': troop_attributes.attack_tier_two_cost,
            'attack_tier_three_name': troop_attributes.attack_tier_three_name,
            'attack_tier_three_power': troop_attributes.attack_tier_three_power,
            'attack_tier_three_cost': troop_attributes.attack_tier_three_cost,
            'defence_tier_one_name': troop_attributes.defence_tier_one_name,
            'defence_tier_one_power': troop_attributes.defence_tier_one_power,
            'defence_tier_one_cost': troop_attributes.defence_tier_one_cost,
            'defence_tier_two_name': troop_attributes.defence_tier_two_name,
            'defence_tier_two_power': troop_attributes.defence_tier_two_power,
            'defence_tier_two_cost': troop_attributes.defence_tier_two_cost,
            'defence_tier_three_name': troop_attributes.defence_tier_three_name,
            'defence_tier_three_power': troop_attributes.defence_tier_three_power,
            'defence_tier_three_cost': troop_attributes.defence_tier_three_cost,
            'intel_tier_one_name': troop_attributes.intel_tier_one_name,
            'intel_tier_one_power': troop_attributes.intel_tier_one_power,
            'intel_tier_one_cost': troop_attributes.intel_tier_one_cost,
            'intel_tier_two_name': troop_attributes.intel_tier_two_name,
            'intel_tier_two_power': troop_attributes.intel_tier_two_power,
            'intel_tier_two_cost': troop_attributes.intel_tier_two_cost,
            'intel_tier_three_name': troop_attributes.intel_tier_three_name,
            'intel_tier_three_power': troop_attributes.intel_tier_three_power,
            'intel_tier_three_cost': troop_attributes.intel_tier_three_cost,
            'income_specialist_name': troop_attributes.income_specialist_name,
            'income_specialist_power': troop_attributes.income_specialist_power,
            'income_specialist_cost': troop_attributes.income_specialist_cost,
            'untrained_name':  troop_attributes.untrained_name,
            'untrained_cost': troop_attributes.untrained_cost,
            'untrained_power': troop_attributes.untrained_power,
        }
        return details
    else:
        # Handle the case where no TroopAttributes exist
        return None  # Or raise an appropriate exception

