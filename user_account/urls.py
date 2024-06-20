from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [

    path('render_user_account', views.render_user_account, name='render_user_account'),
    path('update_user_account', views.update_user_account, name='update_user_account'),
    
]