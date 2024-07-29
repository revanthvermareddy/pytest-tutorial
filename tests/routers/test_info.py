import pytest
from fastapi.testclient import TestClient
from app.main import app

# Create a TestClient instance for the FastAPI app
client = TestClient(app)

def test_get_info():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {
        'app_name': 'PyTest Tutorial',  # Replace with the expected app name or retrieve from a settings fixture
        'admin_email': 'vermareddyrevanth@gmail.com'
    }

# Fixture for providing test-specific settings, if needed
@pytest.fixture
def test_settings():
    # Create a mock or custom settings object if your app depends on specific settings
    from app.config import Settings
    return Settings(app_name="PyTest Tutorial", admin_email="vermareddyrevanth@gmail.com")

def test_get_info_with_fixture(test_settings):
    # If you want to inject custom settings for the test
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {
        'app_name': test_settings.app_name,
        'admin_email': test_settings.admin_email
    }