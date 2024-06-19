from django.shortcuts import render
from django.contrib.auth.models import User

def user_account(request):    
    return render(request, 'user_account/user_account.html')
