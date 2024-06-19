from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('user_account', views.user_account, name='user_account'),
]

