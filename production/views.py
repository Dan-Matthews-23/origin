from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from .models import Production
from user_account.models import UserProfile
from user_account.forms import UserProfileForm
from django.contrib import messages

def production(request):
    profile = UserProfile.objects.get(user=request.user)    
    if not Production.objects.filter(user_profile=profile).exists():
        createItem = Production(
                        user_profile=profile,
                        pop_growth=10,
                        knowledge_points=10,
                        income=10)
        createItem.save()
    getProductionObject = Production.objects.filter(user_profile=profile)
    if getProductionObject.exists():       
        first_production_item = getProductionObject.first()
        getPopGrowth = first_production_item.pop_growth
        log ="Item Found"     
    else:      
        log ="Item not Found"
        getPopGrowth = 0    
    context = {
        'log': log,
        'getPopGrowth': getPopGrowth,
    }
    #print(f"{log}")    
    return render(request, 'production/production.html', context, log)


def increasePopGrowth(request):
    if request.method == 'POST':
        # Get the value from the submitted button
        growth_amount = request.POST.get('growth')  # 'growth' is the name attribute of the button

        if growth_amount:
            profile = UserProfile.objects.get(user=request.user)
            getProductionObject = Production.objects.filter(user_profile=profile)

            if getProductionObject.exists():
                first_production_item = getProductionObject.first()
                try:
                    # Update pop_growth based on the value from the button
                    first_production_item.pop_growth += int(growth_amount)
                    first_production_item.save()
                    messages.success(request, 'Population growth amount increased.')  # Fixed message
                    # Consider using Django's logging framework for more robust logging
                    # print(log)  # Remove this line (log variable not defined)
                    return redirect('production')
                except ValueError:
                    # Handle invalid growth amount
                    messages.error(request, 'Invalid growth amount')
                    return redirect(request.META.get('HTTP_REFERER'))

    ## No valid growth amount submitted or other errors (e.g., GET request)
    return render(request, 'production/production.html', {'error': 'Invalid request'})






