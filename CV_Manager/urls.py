from django.shortcuts import redirect
from django.urls import path
from .views import DashboardView, LogInView, LogOutView

app_name = 'manager'
urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout')
]
