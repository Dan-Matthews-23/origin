
from django.contrib import admin
from .models import Production  


class ProductionAdmin(admin.ModelAdmin):    
    fields = ('user_profile', 'pop_growth', 'knowledge_points', 'knowledge_points_growth', 'income', 'data_crystal_balance')
    list_display = ('user_profile', 'pop_growth', 'knowledge_points', 'knowledge_points_growth', 'income', 'data_crystal_balance')
admin.site.register(Production, ProductionAdmin)

