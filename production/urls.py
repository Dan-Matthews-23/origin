from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('production', views.production, name='production'),
    path('increasePopGrowth', views.increasePopGrowth, name='increasePopGrowth'),
]

