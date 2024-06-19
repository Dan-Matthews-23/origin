from django.shortcuts import render
from django.contrib.auth.models import User

def fight(request):    
    return render(request, 'fight/fight.html')
