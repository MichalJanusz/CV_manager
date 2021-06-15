from django.urls import path
from .views import DashboardView

app_name = 'manager'
urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard')
]
