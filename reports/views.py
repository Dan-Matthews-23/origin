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
from reports.models import IntelLog, AttackLog

from rest_framework import serializers
from .models import IntelLog  # Assuming IntelLog is your model

class ReportSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')  # Specify the desired format
    attacker = serializers.CharField(source='attacker_user_profile.user')
    defender = serializers.CharField(source='defender_user_profile.user')

    class Meta:
        model = IntelLog
        fields = '__all__'  # Include all fields or specify the desired ones

def intel_reports(request):
    profile = UserProfile.objects.get(user=request.user)
    offensive_reports = ReportSerializer(IntelLog.objects.filter(attacker_user_profile=profile), many=True)
    defensive_reports = ReportSerializer(IntelLog.objects.filter(defender_user_profile=profile), many=True)
    context = {'offensive_reports': offensive_reports.data, 'defensive_reports': defensive_reports.data}
    return render(request, 'reports/intel_reports.html', context)


def attack_reports(request):
    profile = UserProfile.objects.get(user=request.user)
    offensive_reports = ReportSerializer(AttackLog.objects.filter(attacker_user_profile=profile), many=True)
    defensive_reports = ReportSerializer(AttackLog.objects.filter(defender_user_profile=profile), many=True)
    context = {'offensive_reports': offensive_reports.data, 'defensive_reports': defensive_reports.data}
    return render(request, 'reports/attack_reports.html', context)























def intel_report_detail(request, report_id):    
    get_report = IntelLog.objects.get(report_id=report_id)
    attacker = get_report.attacker_user_profile.user
    defender = get_report.defender_user_profile.user
    
    report_details = {
        'report_id': get_report.report_id,
        'date': get_report.date,
        'attacker': attacker.username,
        'defender': defender.username,
        'target_attack': get_report.defender_attack_power,
        'target_defence': get_report.defender_defence_power,
        'target_intel': get_report.defender_intel_power,
        'target_income': get_report.defender_income_power,

    } 
    print(report_details)

    context = {'report_details': report_details}
    return render(request, 'reports/intel_report_detail.html', context)


def attack_report_detail(request, report_id):    
    get_report = AttackLog.objects.get(report_id=report_id)
    attacker = get_report.attacker_user_profile.user
    defender = get_report.defender_user_profile.user
    
    report_details = {
        'report_id': get_report.report_id,
        'date': get_report.date,
        'result': get_report.result,
        'defender_user_profile': get_report.defender_user_profile.user,   
        'attacker_user_profile': get_report.attacker_user_profile.user,
        'attacker_t1_loss': get_report.attacker_t1_loss,
        'attacker_t2_loss': get_report.attacker_t2_loss,
        'attacker_t3_loss': get_report.attacker_t3_loss,
        'defender_t1_loss': get_report.defender_t1_loss,
        'defender_t2_loss': get_report.defender_t2_loss,
        'defender_t3_loss': get_report.defender_t3_loss,
        'attacker_t1_count': get_report.attacker_t1_count,
        'attacker_t2_count': get_report.attacker_t2_count,
        'attacker_t3_count': get_report.attacker_t3_count,
        'defender_t1_count': get_report.defender_t1_count,
        'defender_t2_count': get_report.defender_t2_count,
        'defender_t3_count': get_report.defender_t3_count,
        'attacker_attack_snap': get_report.attacker_attack_snap,
        'defender_defence_snap': get_report.defender_defence_snap,
        'data_crystal_gain': get_report.data_crystal_gain, 

    } 
    

    context = {'report_details': report_details}
    return render(request, 'reports/intel_report_detail.html', context)
