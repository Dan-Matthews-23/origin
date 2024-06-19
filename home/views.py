
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User



def index(request):    
    return render(request, 'home/index.html')


def overview(request):    
    return render(request, 'home/overview.html')







