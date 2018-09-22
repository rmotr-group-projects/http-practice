
from http_requests import *


def perform_get_request():
    """Perform GET request to given URL and return the response"""
    url = 'https://httpbin.org/get'
    response = requests.get(url)
    return response

response = perform_get_request()

assert response.status_code == 200
assert response.request.method == 'GET'
assert response.request.url == 'https://httpbin.org/get'
assert 'args' in response.json()
assert response.json()['args'] == {}
assert 'headers' in response.json()
assert 'origin' in response.json()
assert 'url' in response.json()