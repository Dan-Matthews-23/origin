from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    context = { }    
    return render(request, 'home/index.html', context)


@login_required
def overview(request):    
    return render(request, 'home/overview.html')







