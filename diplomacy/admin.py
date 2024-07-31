from django.contrib import admin
from diplomacy.models import Diplomacy, NonAggression, DiplomaticTimeline

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

class NonAggressionAdmin(admin.ModelAdmin):    
    fields = (
        #'date',
        'user',
        'user_accepted',
        'user_rejected',
        'target',
        'target_accepted',
        'target_rejected',
        'length',
        'expired',            
        )
        
    list_display = (
       'date',
        'user',
        'user_accepted',
        'user_rejected',
        'target',
        'target_accepted',
        'target_rejected',
        'length',
        'expired',
        )

class DiplomaticTimelineAdmin(admin.ModelAdmin):    
    fields = (
        #'date',
        'user',        
        'target',
        'event_message_user',
        'event_message_target',                 
        )
        
    list_display = (
       'date',
        'user',        
        'target',
        'event_message_user',
        'event_message_target',
        )


admin.site.register(Diplomacy, DiplomacyAdmin)
admin.site.register(NonAggression, NonAggressionAdmin)
admin.site.register(DiplomaticTimeline, DiplomaticTimelineAdmin)

