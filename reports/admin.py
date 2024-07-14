from django.contrib import admin


from .models import IntelLog


class IntelLogAdmin(admin.ModelAdmin):    
    fields = (
        'report_id',
        'date',
        'result', 
        'defender_user_profile', 
        'defender_intel',
        'defender_troops', 
        'defender_technologies', 
        'defender_bonus',
        'attacker_user_profile', 
        'attacker_intel', 
        'attacker_troops',
        'attacker_technologies',
        'attacker_bonus',
        'attacker_weak_intel_troops_loss', 
        'attacker_strong_intel_troops_loss', 
        'attacker_elite_intel_troops_loss',
        'defender_defence_power', 
        'defender_attack_power',
        'defender_intel_power', 
        'defender_income_power',  
        'defender_weak_attack_troops', 
        'defender_strong_attack_troops',  
        'defender_elite_attack_troops',  
        'defender_weak_defence_troops',  
        'defender_strong_defence_troops', 
        'defender_elite_defence_troops',  
        'defender_weak_intel_troops',  
        'defender_strong_intel_troops',  
        'defender_elite_intel_troops',  
        'defender_income_specialists',  
        'defender_untrained_units',
        )
        
    list_display = (
        'report_id',
        'date',
        'result', 
        'defender_user_profile', 
        'defender_intel',
        'defender_troops', 
        'defender_technologies', 
        'defender_bonus',
        'attacker_user_profile', 
        'attacker_intel', 
        'attacker_troops',
        'attacker_technologies',
        'attacker_bonus',
        'attacker_weak_intel_troops_loss', 
        'attacker_strong_intel_troops_loss', 
        'attacker_elite_intel_troops_loss',
        'defender_defence_power', 
        'defender_attack_power',
        'defender_intel_power', 
        'defender_income_power',  
        'defender_weak_attack_troops', 
        'defender_strong_attack_troops',  
        'defender_elite_attack_troops',  
        'defender_weak_defence_troops',  
        'defender_strong_defence_troops', 
        'defender_elite_defence_troops',  
        'defender_weak_intel_troops',  
        'defender_strong_intel_troops',  
        'defender_elite_intel_troops',  
        'defender_income_specialists',  
        'defender_untrained_units',  
        )
admin.site.register(IntelLog, IntelLogAdmin)


