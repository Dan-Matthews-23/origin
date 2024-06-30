from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from .models import Production
from user_account.models import UserProfile
from user_account.forms import UserProfileForm
from django.contrib import messages
from django.conf import settings
from military.views import getTroopNumbers

def production(request):
    profile = UserProfile.objects.get(user=request.user)
    try:
        production_object = Production.objects.get(user_profile=profile)
       
        # Render Pop Growth
        pop_growth = production_object.pop_growth        
        getPopGrowthByTen = pop_growth + 10
        increaseProjectionByTenCost = "{:,d}".format(getPopGrowthByTen * settings.BASE_POP_INCREASE_COST)
        getPopGrowthByHundred = pop_growth + 100
        increaseProjectionByHundredCost = "{:,d}".format(getPopGrowthByHundred * settings.BASE_POP_INCREASE_COST)
        getPopGrowthByThousand = pop_growth + 1000
        increaseProjectionByThousandCost = "{:,d}".format(getPopGrowthByThousand * settings.BASE_POP_INCREASE_COST)

        #Render Income Growth       
        income_growth = production_object.income       
        getIncomeByTen = income_growth + 10
        increaseProjectionByTenCostIncome = "{:,d}".format(getIncomeByTen * settings.BASE_POP_INCREASE_COST)
        getIncomeByHundred = income_growth + 100
        increaseProjectionByHundredCostIncome = "{:,d}".format(getIncomeByHundred * settings.BASE_POP_INCREASE_COST)
        getIncomeByThousand = income_growth + 1000
        increaseProjectionByThousandCostIncome = "{:,d}".format(getIncomeByThousand * settings.BASE_POP_INCREASE_COST)

        #Render Knowledge Points Growth       
        knowledge_growth = production_object.knowledge_points       
        getKnowledgeByTen = knowledge_growth + 10
        increaseProjectionByTenCostKnowledge = "{:,d}".format(getKnowledgeByTen * settings.BASE_POP_INCREASE_COST)
        getKnowledgeByHundred = knowledge_growth + 100
        increaseProjectionByHundredCostKnowledge = "{:,d}".format(getKnowledgeByHundred * settings.BASE_POP_INCREASE_COST)
        getKnowledgeByThousand = knowledge_growth + 1000
        increaseProjectionByThousandCostKnowledge = "{:,d}".format(getKnowledgeByThousand * settings.BASE_POP_INCREASE_COST)
    
    
    
    except Production.DoesNotExist:       
        production_object = Production.objects.create(
            user_profile=profile,
            pop_growth=10,
            knowledge_points=10,
            income=10
        )
        pop_growth = production_object.pop_growth
        income_growth = production_object.income
        knowledge_growth = production_object.knowledge_points

    troopNumbers = getTroopNumbers(request)
    

    context = {
        'getPopGrowth': pop_growth,
        'getPopGrowthByTen': getPopGrowthByTen,
        'increaseProjectionByTen': increaseProjectionByTenCost,
        'getPopGrowthByHundred': getPopGrowthByHundred,
        'increaseProjectionByHundred': increaseProjectionByHundredCost,
        'getPopGrowthByThousand': getPopGrowthByThousand,
        'increaseProjectionByThousand': increaseProjectionByThousandCost,        
        'getIncomeGrowth': income_growth,
        'getIncomeByTen': getIncomeByTen,
        'increaseProjectionByTenIncome': increaseProjectionByTenCostIncome,
        'getIncomeByHundred': getIncomeByHundred,
        'increaseProjectionByHundredIncome': increaseProjectionByHundredCostIncome,
        'getIncomeByThousand': getIncomeByThousand,
        'increaseProjectionByThousandIncome': increaseProjectionByThousandCostIncome,
        'getKnowledgeGrowth': knowledge_growth,
        'getKnowledgeByTen': getKnowledgeByTen,
        'increaseProjectionByTenKnowledge': increaseProjectionByTenCostKnowledge,
        'getKnowledgeByHundred': getKnowledgeByHundred,
        'increaseProjectionByHundredKnowledge': increaseProjectionByHundredCostKnowledge,
        'getKnowledgeByThousand': getKnowledgeByThousand,
        'increaseProjectionByThousandKnowledge': increaseProjectionByThousandCostKnowledge,
        'troopNumbers': troopNumbers,
    }
    return render(request, 'production/production.html', context)













def increasePopGrowth(request):
    base_cost = settings.BASE_POP_INCREASE_COST
    if request.method == 'POST':
        growth_amount = int(request.POST.get('growth'))
        if growth_amount:
            profile = request.user.userprofile
            production_object = Production.objects.get(user_profile=profile)
            growth_cost = ((production_object.pop_growth + growth_amount) * base_cost)
            if production_object.data_crystal_balance >= growth_cost:
                production_object.pop_growth += growth_amount
                production_object.data_crystal_balance -= growth_cost
                production_object.save()
                messages.success(request, 'Population growth amount increased.')
                print(f"The population growth was increased by {growth_amount} at a cost of {growth_cost}")
                return redirect('production')
            else:
                messages.error(request, 'Insufficient resources for population growth increase.')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'No growth amount was selected')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'production/production.html')














def increaseIncome(request):
    base_cost = settings.BASE_POP_INCREASE_COST
    if request.method == 'POST':
        growth_amount = int(request.POST.get('income'))
        if growth_amount:
            profile = request.user.userprofile
            production_object = Production.objects.get(user_profile=profile)
            growth_cost = ((production_object.income + growth_amount) * base_cost)
            if production_object.data_crystal_balance >= growth_cost:
                production_object.income += growth_amount
                production_object.data_crystal_balance -= growth_cost
                production_object.save()
                messages.success(request, 'Data Crystal production  increased.')                
                return redirect('production')
            else:
                messages.error(request, 'Insufficient resources for data crystal production increase.')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'No data crystal production amount was selected')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'production/production.html')




def increaseKnowledge(request):
    base_cost = settings.BASE_POP_INCREASE_COST
    if request.method == 'POST':
        growth_amount = int(request.POST.get('knowledge'))
        if growth_amount:
            profile = request.user.userprofile
            production_object = Production.objects.get(user_profile=profile)
            growth_cost = ((production_object.knowledge_points + growth_amount) * base_cost)
            if production_object.data_crystal_balance >= growth_cost:
                production_object.knowledge_points += growth_amount
                production_object.data_crystal_balance -= growth_cost
                production_object.save()
                messages.success(request, 'Knowledge point production increased.')                
                return redirect('production')
            else:
                messages.error(request, 'Insufficient resources for Knowledge point production increase.')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'No Knowledge point production amount was selected')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'production/production.html')









