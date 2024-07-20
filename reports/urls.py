from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('intel_reports', views.intel_reports, name='intel_reports'),    
    path('attack_reports', views.attack_reports, name='attack_reports'),
    path('intel_report_detail/<report_id>/', views.intel_report_detail, name='intel_report_detail'),
    path('attack_report_detail/<report_id>/', views.attack_report_detail, name='attack_report_detail'),
    

]