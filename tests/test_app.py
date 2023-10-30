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

import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    return app.test_client()

def test_main_route(client):
    """Test the main route."""
    response = client.get('/')
    assert response.status_code == 200
    assert 'Welcome!' in response.data.decode('utf-8')

def test_hello_route(client):
    """Test the hello route."""
    response = client.get('/how%20are%20you')  # Use URL-encoded format for spaces
    assert response.status_code == 200
    assert 'I am good, how about you?' in response.data.decode('utf-8')

