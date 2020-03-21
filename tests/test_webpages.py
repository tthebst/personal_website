import sys
sys.path.insert(0, '..')
from app import app
import pytest

def test_assert():
    assert True

def test_home_page(client):
  response = client.get('/')
  assert response.status_code == 200

def test_wallpapers(client):
  response = client.get('/wallpapers')
  assert response.status_code == 200

def test_wallpapers_all(client):
  response = client.get('/wallpapers_all')
  assert response.status_code == 200




@pytest.fixture
def client():
  client = app.test_client()
  return client