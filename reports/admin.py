from django.contrib import admin


from .models import IntelLog


class IntelLogAdmin(admin.ModelAdmin):    
    fields = (
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

        )
        
    list_display = (
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
        )
admin.site.register(IntelLog, IntelLogAdmin)


