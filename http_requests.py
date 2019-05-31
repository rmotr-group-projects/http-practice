import requests


def perform_get_request():
    """Perform GET request to given URL and return the response"""
    url = 'https://httpbin.org/get'
    response = requests.get(url)
    return response


def perform_get_request_with_params():
    """Perform GET request to given URL sending any parameter and return the response"""
    # HINT: you should add the GET parameters at the end of the url
    url = 'https://httpbin.org/get'
    response = requests.get(url, params = {'user':'Jocelyn'})
    return response


def perform_post_request():
    """Perform POST request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/post'
    data = {
        'first_name': 'Guido',
        'last_name': 'van Rossum'
    }
    resp = requests.post(url, json = data)
    resp.json()
    return resp

def perform_put_request():
    """Perform PUT request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/put'
    data = {
        'first_name': 'Guido',
        'last_name': 'van Rossum'
    }
    resp = requests.put(url, json = data)
    resp.json()
    return resp

def perform_patch_request():
    """Perform PATCH request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/patch'
    data = {
        'first_name': 'Guido'
    }
    resp = requests.patch(url, json = data)
    resp.json()
    return resp


def perform_delete_request():
    """Perform DELETE request to given URL and return the response"""
    url = 'https://httpbin.org/delete'
    resp = requests.delete(url)
    resp.json()
    return resp


def perform_redirect_request():
    """Perform a request to a redirect URL and return the Location header that come in the response"""
    # HINT: you should use the allow_redirects parameter while doing the request
    url = 'https://httpbin.org/redirect/1'
    resp = requests.get(url, allow_redirects = False)
    return resp.headers['location']
