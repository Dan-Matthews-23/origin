
from django.contrib import admin
from .models import Production  


class ProductionAdmin(admin.ModelAdmin):    
    fields = ('user_profile', 'pop_growth', 'knowledge_points', 'income')
    list_display = ('user_profile', 'pop_growth', 'knowledge_points', 'income')
admin.site.register(Production, ProductionAdmin)

