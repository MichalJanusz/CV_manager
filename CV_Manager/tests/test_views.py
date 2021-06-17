import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer
from CV_Manager.models import User
from CV_Manager.views import DashboardView


@pytest.mark.django_db
class TestViews:

    def test_dashboard_authenticated(self, client, rf):
        path = reverse('manager:dashboard')
        request = rf.get(path)
        request.user = mixer.blend(User)
        client.force_login(request.user)
        # This is one way to test class based views - using client fixture, also used request factory fixture

        response = client.get(path)
        assert response.status_code == 200

    def test_dashboard_unauthenticated(self):
        path = reverse('manager:dashboard')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()
        # This is the other way to test class based views - using the as_view() method

        response = DashboardView.as_view()(request)
        assert '/login' in response.url
