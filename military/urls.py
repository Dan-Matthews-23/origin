from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('military', views.military, name='military'),
]

