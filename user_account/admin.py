from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        field_names = [field.name for field in UserProfile._meta.fields]
        return field_names
    ordering = ('user_id',)


admin.site.register(UserProfile, UserProfileAdmin)