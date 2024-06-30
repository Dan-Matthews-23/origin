from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from production.models import Production
import time










def active_user_count(request):
    threshold = timezone.now() - timezone.timedelta(minutes=30)
    active_user_count = User.objects.filter(last_login__gte=threshold).count()
    return {'active_user_count': active_user_count}


def data_crystal_balance(request):
    if request.user.is_authenticated:
        profile = request.user.userprofile
        
        try:
            production_object = Production.objects.get(user_profile=profile)
            data_crystal_balance = production_object.data_crystal_balance
            data_crystal_balance = "{:,d}".format(data_crystal_balance)
            return {'data_crystal_balance': data_crystal_balance}
        except Production.DoesNotExist:
            return {'data_crystal_balance': 0}
    else:
        # Set a default value or message for unauthenticated users
        return {'data_crystal_balance': 'N/A'}  # Or any suitable message

    

