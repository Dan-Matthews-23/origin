# home/context_processors.py

from django.contrib.auth.models import User
from django.utils import timezone

def active_user_count(request):
    threshold = timezone.now() - timezone.timedelta(minutes=30)
    active_user_count = User.objects.filter(last_login__gte=threshold).count()
    return {'active_user_count': active_user_count}
