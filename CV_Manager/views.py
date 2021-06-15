from django.shortcuts import render

# Create your views here.
from django.views import View


class DashboardView(View):
    def get(self, request):
        return render(request, 'CV_Manager/dashboard.html', {'page': 'home'})

