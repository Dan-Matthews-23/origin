from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('diplomacy', views.diplomacy, name='diplomacy'),
    path('make_ally/<player_id>/', views.make_ally, name='make_ally'),
    path('make_enemy/<player_id>/', views.make_enemy, name='make_enemy'),
    path('diplomatic_info/<player_id>/', views.diplomatic_info, name='diplomatic_info'),
]

