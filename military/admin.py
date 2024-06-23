from django.contrib import admin
from .models import Troops


class TroopsAdmin(admin.ModelAdmin):    
    fields = (
        'weak_attack_troops', 
        'strong_attack_troops', 
        'elite_attack_troops',
        'weak_defence_troops', 
        'strong_defence_troops', 
        'elite_defence_troops',
        'weak_intel_troops', 
        'strong_intel_troops', 
        'elite_intel_troops',
        'income_specialists', 
        'untrained_units',        
        )
        
    list_display = (
        'weak_attack_troops', 
        'strong_attack_troops', 
        'elite_attack_troops',
        'weak_defence_troops', 
        'strong_defence_troops', 
        'elite_defence_troops',
        'weak_intel_troops', 
        'strong_intel_troops', 
        'elite_intel_troops',
        'income_specialists', 
        'untrained_units',
        )
admin.site.register(Troops, TroopsAdmin)