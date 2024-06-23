from django.contrib import admin
from .models import PlayerPower


class PlayerPowerAdmin(admin.ModelAdmin):    
    fields = (
        'attack', 
        'defence', 
        'intel',
        'income', 
        'attack_rank', 
        'defence_rank',
        'intel_rank', 
        'income_rank', 
        'overall_rank',              
        )
        
    list_display = (
        'attack', 
        'defence', 
        'intel',
        'income', 
        'attack_rank', 
        'defence_rank',
        'intel_rank', 
        'income_rank', 
        'overall_rank', 
        )
admin.site.register(PlayerPower, PlayerPowerAdmin)