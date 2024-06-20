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
            try:
                growth_amount = int(growth_amount)
            except ValueError:
                messages.error(request, 'Invalid growth amount')
                return redirect(request.META.get('HTTP_REFERER'))

            profile = request.user.userprofile  # Assuming UserProfile model is linked to User

            try:
                production_object = Production.objects.get(user_profile=profile)
                data_crystal_balance = production_object.data_crystal_balance
                print(f"Data crystal balance is {data_crystal_balance}")

                # Calculate costs efficiently
                cost_by_growth = {
                    10: growth_amount * base_cost,
                    100: growth_amount * base_cost * 10,
                    1000: growth_amount * base_cost * 100
                }

                # Check affordability for all options
                affordable_option = None
                for increase, cost in cost_by_growth.items():
                    if data_crystal_balance >= cost:
                        affordable_option = increase
                        break

                if affordable_option:
                    data_crystal_balance -= cost_by_growth[affordable_option]
                    production_object.pop_growth += growth_amount
                    production_object.data_crystal_balance = data_crystal_balance
                    production_object.save()

                    messages.success(request, 'Population growth amount increased.')
                    return redirect('production')
                else:
                    messages.error(request, 'You cannot afford any of the options.')
            except Production.DoesNotExist:
                messages.error(request, 'Production object not found.')
            except Exception as e:  # Catch broader exceptions for better error handling
                messages.error(request, 'An error occurred. Please try again later.')

    return redirect(request.META.get('HTTP_REFERER'))







