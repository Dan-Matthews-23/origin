from django.db import models
from user_account.models import UserProfile

class ErrorLog(models.Model):
    log_id = models.AutoField(primary_key=True, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='user_error')
    app = models.CharField(max_length=80, null=True, blank=True)
    function = models.CharField(max_length=80, null=True, blank=True)
    error = models.TextField(null=True, blank=True)
    
