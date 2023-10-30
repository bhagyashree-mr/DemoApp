# import pytest
# from app import app

# @pytest.fixture
# def client():
#     """Create a test client for the Flask application."""
#     return app.test_client()

# def test_main_route(client):
#     """Test the main route."""
#     response = client.get('/')
#     assert response.status_code == 200
#     assert b'Welcome!' in response.data

# def test_hello_route(client):
#     """Test the hello route."""
#     response = client.get('/how are you')
#     assert response.status_code == 200
#     assert b'I am good, how about you?' in response.data

# tests/test_app.py
from DEMOWEBAPP.app.app import app  # Assuming your Flask app is defined in app.py

import pytest

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    return app.test_client()

def test_main_route(client):
    """Test the main route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome!' in response.data

def test_hello_route(client):
    """Test the hello route."""
    response = client.get('/how are you')
    assert response.status_code == 200
    assert b'I am good, how about you?' in response.data


