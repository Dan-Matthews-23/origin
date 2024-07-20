from django.contrib import admin
from error_log.models import ErrorLog

class ErrorLogAdmin(admin.ModelAdmin):    
    fields = ('log_id', 'date', 'user', 'app', 'function', 'error')
    list_display = ('log_id', 'date', 'user', 'app', 'function', 'error')
admin.site.register(ErrorLog, ErrorLogAdmin)
