from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('renderMilitary', views.renderMilitary, name='renderMilitary'),
    path('trainTroops', views.trainTroops, name='trainTroops'),
    

]