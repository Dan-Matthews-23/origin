from django.contrib import admin
from django.urls import path
from . import views

#app_name = 'fight'

urlpatterns = [
    path('fight', views.fight, name='fight'),
    path('player_info/<player_id>/', views.player_info, name='player_info'),
    path('spy/<player_id>/', views.spy, name='spy'),
    path('attack/<player_id>/', views.attack, name='attack'),
    
]

