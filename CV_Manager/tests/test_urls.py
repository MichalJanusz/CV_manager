import pytest
from django.urls import reverse, resolve
# Create your tests here.


class TestUrls:

    @pytest.mark.parametrize('name', [
        'manager:dashboard',
        'manager:login',
        'manager:logout',
    ])
    def test_dashboard_url(self, name):
        path = reverse(name)
        assert resolve(path).view_name == name
