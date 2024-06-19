from django.shortcuts import render
from django.contrib.auth.models import User

def production(request):    
    return render(request, 'production/production.html')
