from django.contrib.auth.models import User
from django.utils import timezone
from production.models import Production

def active_user_count(request):
    threshold = timezone.now() - timezone.timedelta(minutes=30)
    active_user_count = User.objects.filter(last_login__gte=threshold).count()
    return {'active_user_count': active_user_count}

def data_crystal_balance(request):
    try:
        profile = request.user.userprofile
        production_object = Production.objects.get(user_profile=profile)
        data_crystal_balance = production_object.data_crystal_balance
        data_crystal_balance = "{:,d}".format(data_crystal_balance)
        return {'data_crystal_balance': data_crystal_balance}
    except Production.DoesNotExist:
        # No need for production_object here, return 0 directly
        return {'data_crystal_balance': 0}

