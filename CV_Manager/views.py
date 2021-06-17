from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View


class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'CV_Manager/dashboard.html')


class LogInView(LoginView):

    template_name = 'CV_Manager/login.html'


class LogOutView(LogoutView):
    pass
