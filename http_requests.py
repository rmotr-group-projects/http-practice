import requests


def perform_get_request():
    """Perform GET request to given URL and return the response"""
    url = 'https://httpbin.org/get'
    response = requests.get(url)
    return response


def perform_get_request_with_params():
    url = 'https://httpbin.org/get'
    response = requests.get(url, params={'user_id': '123'})
    return response


def perform_post_request():
    url = 'https://httpbin.org/post'
    data = {
        'first_name': 'Guido',
        'last_name': 'van Rossum'
    }
    response = requests.post(url, json=data)
    return response


def perform_put_request():
    url = 'https://httpbin.org/put'
    data = {
        'first_name': 'Guido',
        'last_name': 'van Rossum'
    }
    response = requests.put(url, json=data)
    return response


def perform_patch_request():
    url = 'https://httpbin.org/patch'
    data = {
        'first_name': 'Guido'
    }
    response = requests.patch(url, json=data)
    return response


def perform_delete_request():
    url = 'https://httpbin.org/delete'
    response = requests.delete(url)
    return response


def perform_redirect_request():
    url = 'https://httpbin.org/redirect/1'
    
    response = requests.get(url, allow_redirects=False)
    return response.headers['Location']
