'''
Test for GET ping route
'''
import requests

BASE_URL = 'http://localhost'


def test_get_ping_returns_200():
    response = requests.get(BASE_URL + '/ping')
    assert response.status_code == 200
