from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('diplomacy', views.diplomacy, name='diplomacy'),
]

