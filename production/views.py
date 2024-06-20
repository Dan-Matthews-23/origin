from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from .models import Production
from user_account.models import UserProfile
from user_account.forms import UserProfileForm
from django.contrib import messages
from django.conf import settings

def production(request):
    base_cost = settings.BASE_POP_INCREASE_COST
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
        getPopGrowthByTen = getPopGrowth
        getPopGrowthByHundred = getPopGrowth
        getPopGrowthByThousand = getPopGrowth

        getPopGrowthByTen += 10
        increaseProjectionByTen = "{:,d}".format(getPopGrowthByTen * base_cost)        

        getPopGrowthByHundred += 100
        increaseProjectionByHundred = "{:,d}".format(getPopGrowthByHundred * base_cost) 

        getPopGrowthByThousand += 1000
        increaseProjectionByThousand = "{:,d}".format(getPopGrowthByThousand * base_cost) 

        log ="Item Found"     
    else:      
        log ="Item not Found"
        getPopGrowth = 0    
    context = {
        'log': log,
        'getPopGrowth': getPopGrowth,

        'getPopGrowthByTen':getPopGrowthByTen,
        'increaseProjectionByTen':increaseProjectionByTen,

        'getPopGrowthByHundred':getPopGrowthByHundred,
        'increaseProjectionByHundred':increaseProjectionByHundred,

        'getPopGrowthByThousand':getPopGrowthByThousand,
        'increaseProjectionByThousand':increaseProjectionByThousand,
    }      
    return render(request, 'production/production.html', context, log)


def increasePopGrowth(request):
    base_cost = settings.BASE_POP_INCREASE_COST
    if request.method == 'POST':       
        growth_amount = request.POST.get('growth')
        if growth_amount:
            profile = UserProfile.objects.get(user=request.user)
            getProductionObject = Production.objects.filter(user_profile=profile)
            if getProductionObject.exists():
                first_production_item = getProductionObject.first()
                #cost = (first_production_item * base_cost)
                try:                    
                    first_production_item.pop_growth += int(growth_amount)
                    first_production_item.save()
                    messages.success(request, 'Population growth amount increased.')                    
                    return redirect('production')
                except ValueError:                   
                    messages.error(request, 'Invalid growth amount')
                    return redirect(request.META.get('HTTP_REFERER'))   
    messages.error(request, ('There was an\
            error prcocessing. Please try again in a few minutes'))
    return redirect(request.META.get('HTTP_REFERER'))






