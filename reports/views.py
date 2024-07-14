from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from user_account.models import UserProfile
from player_power.models import PlayerPower
from military.models import Troops
from production.models import Production
from military.views import calculate_total_troops
from django.db.models import Sum, Q
import random
from random import choice
from django.conf import settings
from reports.models import IntelLog

from django.shortcuts import render

def reports(request):
    profile = UserProfile.objects.get(user=request.user)

    # Efficiently filter IntelLogs for both offensive and defensive reports
    reports_query = IntelLog.objects.filter(
        Q(attacker_user_profile=profile) | Q(defender_user_profile=profile)
    ).select_related('attacker_user_profile', 'defender_user_profile')  # Optimize for related fields

    # Extract report data with concise dictionary comprehension
    reports = {
        'offensive': [
            {
                'report_id': report.report_id,
                'date': report.date,
                'result': report.result,
                'attacker_intel': report.attacker_intel,
                'attacker_troops': report.attacker_troops,
                'attacker_technologies': report.attacker_technologies,
                'attacker_bonus': report.attacker_bonus,
                'attacker': "You",
                'defender': report.defender_user_profile.user,
            }
            for report in reports_query.filter(attacker_user_profile=profile)
        ],
        'defensive': [
            {
                'report_id': report.report_id,
                'date': report.date,
                'result': report.result,
                'defender_intel': report.defender_intel,
                'defender_troops': report.defender_troops,
                'defender_technologies': report.defender_technologies,
                'defender_bonus': report.defender_bonus,
                'defender': defender_user_profile,
            }
            for report in reports_query.filter(defender_user_profile=profile)
        ],
    }

    context = {'reports': reports}
    return render(request, 'reports/reports.html', context)

















def report_detail(request, report_id):    
    get_report = IntelLog.objects.get(report_id=report_id)
    attacker = get_report.attacker_user_profile.user
    defender = get_report.defender_user_profile.user
    
    report_details = {
        'report_id': get_report.report_id,
        'date': get_report.date,
        'attacker': attacker,
        'defender': defender,

    } 
    print(report_details)

    context = {'report_details': report_details}
    return render(request, 'reports/report_detail.html', context)
