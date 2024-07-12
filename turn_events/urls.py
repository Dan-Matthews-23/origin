from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('initiate_turn_event', views.initiate_turn_event, name='initiate_turn_event'),
   
]

