from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from game_settings.views import get_user, get_player, get_diplomacy, get_non_aggression_pacts#, create_non_aggression_pact
from django.contrib import messages
from diplomacy.models import NonAggression, DiplomaticTimeline
from game_settings.base_mods import diplomatic_timeline_events

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

def diplomatic_info(request, player_id):
    active = False
    user = get_user(request)
    player = get_player(request, player_id)
    pact_query = get_non_aggression_pacts(request, user, player)

    if pact_query:
        active = True
        if pact_query.user_accepted == True and pact_query.target_accepted == True:
            pending_agression = {
                'date': pact_query.date,
                'status': "Active Pact",
            }
        elif pact_query.user_accepted == False or pact_query.target_accepted == False:
            pending_agression = {
                'date': pact_query.date,
                'status': "Has not been accepted by both parties",
            }
        else:  # Add this new condition
            pending_agression = {
                'date': pact_query.date,
                'status': "Pending",
            }
    else:
        active = False
        pending_agression = {}
    
    player_info = {
        'player_id': player_id
    }
    context = {'player_info': player_info, 'pending_agression': pending_agression, 'active': active}
    return render(request, 'diplomacy/diplomatic_info.html', context)


def non_aggression_pact(request, player_id):
    event = "Propose Non-Aggression Pact"
    user = get_user(request)
    player = get_player(request, player_id)
    pact_query = get_non_aggression_pacts(request, user, player)

    if pact_query:
        messages.error(request, "You already have a non-aggression pact with this user")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        create = create_non_aggression_pact(request, user, player)

        event_dictionary = diplomatic_timeline_events(request)
        event_message_user = event_dictionary[event]["user_event"]
        event_message_target = event_dictionary[event]["target_event"]
        create_event = add_diplomatic_timeline_event(request, user, player, event_message_user, event_message_target)

        messages.success(request, "Awaiting acceptance")
        return redirect(request.META.get('HTTP_REFERER'))


    
def create_non_aggression_pact(request, user, player):
    create_pact = NonAggression.objects.create(
            user=user,
            user_accepted=True,
            target=player,
            target_accepted=False,
            length=1440,
            expired=False,
        )


def add_diplomatic_timeline_event(request, user, player, event_message_user, event_message_target):
    query = DiplomaticTimeline.objects.create(
            user=user,           
            target=player,
            event_message_target=event_message_target,
            event_message_user=event_message_user,
        )