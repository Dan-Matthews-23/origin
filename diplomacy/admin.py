from django.contrib import admin
from diplomacy.models import Diplomacy

class DiplomacyAdmin(admin.ModelAdmin):    
    fields = (
        'date',
        'user', 
        'target', 
        'relation',               
        )
        
    list_display = (
       'date',
        'user', 
        'target', 
        'relation',
        )
admin.site.register(Diplomacy, DiplomacyAdmin)
