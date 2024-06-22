
from django.contrib import admin
from .models import TroopAttributes  


class TroopAttributesAdmin(admin.ModelAdmin):    
    fields = (
        'attack_tier_one_name', 
        'attack_tier_one_power', 
        'attack_tier_one_cost',
        'attack_tier_two_name', 
        'attack_tier_two_power', 
        'attack_tier_two_cost',
        'attack_tier_three_name', 
        'attack_tier_three_power', 
        'attack_tier_three_cost',
        'defence_tier_one_name', 
        'defence_tier_one_power', 
        'defence_tier_one_cost',
        'defence_tier_two_name', 
        'defence_tier_two_power', 
        'defence_tier_two_cost',
        'defence_tier_three_name', 
        'defence_tier_three_power', 
        'defence_tier_three_cost',
        'intel_tier_one_name', 
        'intel_tier_one_power', 
        'intel_tier_one_cost',
        'intel_tier_two_name', 
        'intel_tier_two_power', 
        'intel_tier_two_cost',
        'intel_tier_three_name', 
        'intel_tier_three_power', 
        'intel_tier_three_cost',
        'income_specialist_name',        
        'income_specialist_power',
        'income_specialist_cost',
        )
        
    list_display = (
        'attack_tier_one_name', 
        'attack_tier_one_power', 
        'attack_tier_one_cost',
        'attack_tier_two_name', 
        'attack_tier_two_power', 
        'attack_tier_two_cost',
        'attack_tier_three_name', 
        'attack_tier_three_power', 
        'attack_tier_three_cost',
        'defence_tier_one_name', 
        'defence_tier_one_power', 
        'defence_tier_one_cost',
        'defence_tier_two_name', 
        'defence_tier_two_power', 
        'defence_tier_two_cost',
        'defence_tier_three_name', 
        'defence_tier_three_power', 
        'defence_tier_three_cost',
        'intel_tier_one_name', 
        'intel_tier_one_power', 
        'intel_tier_one_cost',
        'intel_tier_two_name', 
        'intel_tier_two_power', 
        'intel_tier_two_cost',
        'intel_tier_three_name', 
        'intel_tier_three_power', 
        'intel_tier_three_cost',
        'income_specialist_name',        
        'income_specialist_power',
        'income_specialist_cost', 
        )
admin.site.register(TroopAttributes, TroopAttributesAdmin)




    
    