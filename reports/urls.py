from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('reports', views.reports, name='reports'),
    path('report_detail/<report_id>/', views.report_detail, name='report_detail'),
    

]