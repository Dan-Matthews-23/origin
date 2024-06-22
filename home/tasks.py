from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from .models import Production
from user_account.models import UserProfile
from user_account.forms import UserProfileForm
from django.contrib import messages
from django.conf import settings


"""
def updateAllPlayers(request):
    for production_object in Production.objects.get():
        pop_growth += production_object.pop_growth
        knowledge_points = production_object.knowledge_points
        income = production_object.income
        data_crystal_balance = production_object.data_crystal_balance
        """

       




   

