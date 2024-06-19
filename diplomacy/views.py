from django.shortcuts import render
from django.contrib.auth.models import User

def diplomacy(request):    
    return render(request, 'diplomacy/diplomacy.html')
