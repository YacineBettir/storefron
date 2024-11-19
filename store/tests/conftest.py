from rest_framework.test import APIClient
import pytest

from core.models import User


@pytest.fixture
def client_api():
    return APIClient()

@pytest.fixture
def authenticate_users(client_api):
    def do_authenticate(is_staff=False):
        return client_api.force_authenticate(user=User(is_staff=is_staff))
    return do_authenticate