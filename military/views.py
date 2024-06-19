from django.shortcuts import render
from django.contrib.auth.models import User

def military(request):    
    return render(request, 'military/military.html')
