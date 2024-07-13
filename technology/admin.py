

from django.contrib import admin
from .models import UserTechnology, TechnologyCategory, Civilization, ResearchableTechnology



class UserTechnologyAdmin(admin.ModelAdmin):    
    fields = ('technology', 'research_completed', 'research_points')
    list_display = ('technology', 'research_completed', 'research_points')
admin.site.register(UserTechnology, UserTechnologyAdmin)

class TechnologyCategoryAdmin(admin.ModelAdmin):    
    fields = ('name',)
    list_display = ('name', )
admin.site.register(TechnologyCategory, TechnologyCategoryAdmin)

class CivilizationAdmin(admin.ModelAdmin):    
    fields = ('name', )
    list_display = ('name', )
admin.site.register(Civilization, CivilizationAdmin)

class ResearchableTechnologyAdmin(admin.ModelAdmin):    
    fields = ('name', 'category', 'cost', 'level', 'is_unique', 'unique_to')
    list_display = ('name', 'category', 'cost', 'level', 'is_unique', 'unique_to')
admin.site.register(ResearchableTechnology, ResearchableTechnologyAdmin)
