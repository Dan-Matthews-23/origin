
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def overview(request):
    threshold = timezone.now() - timezone.timedelta(minutes=30)
    active_user_count = User.objects.filter(last_login__gte=threshold).count()
    context = {'active_user_count': active_user_count}
    return render(request, 'home/overview.html', context)







