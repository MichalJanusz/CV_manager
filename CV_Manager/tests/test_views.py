import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer
from pytest_django.asserts import assertTemplateUsed
from CV_Manager.models import User
from CV_Manager.views import DashboardView

@pytest.fixture
def dashboard_path():
    return reverse('manager:dashboard')

@pytest.mark.django_db
class TestViews:

    def test_dashboard_authenticated(self, client, rf, dashboard_path):
        request = rf.get(dashboard_path)
        request.user = mixer.blend(User)
        client.force_login(request.user)
        # This is one way to test class based views - using client fixture, also used request factory fixture

        response = client.get(dashboard_path)
        assert response.status_code == 200

    def test_dashboard_unauthenticated(self, dashboard_path):
        request = RequestFactory().get(dashboard_path)
        request.user = AnonymousUser()
        # This is the other way to test class based views - using the as_view() method

        response = DashboardView.as_view()(request)
        assert '/login' in response.url

    def test_dashboard_uses_correct_template(self, client, dashboard_path, rf):
        client.force_login(mixer.blend(User))
        response = client.get(dashboard_path)
        print()
        assertTemplateUsed(response, 'CV_Manager/dashboard.html')

