import requests


def perform_get_request():
    """Perform GET request to given URL and return the response"""
    url = 'https://httpbin.org/get'
    response = requests.get(url)
    return response
#ok


def perform_get_request_with_params():
    """Perform GET request to given URL sending any parameter and return the response"""
    # HINT: you should add the GET parameters at the end of the url
    url = 'https://httpbin.org/get'
    params_example = {'key1' : 'value1'}
    request_with_params = requests.get ('https://httpbin.org/get', params = params_example)
    return request_with_params
#ok

def perform_post_request():
    """Perform POST request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/post'
    data_example = {'first_name': 'Guido','last_name': 'van Rossum'}
    post_request = requests.post ('https://httpbin.org/post', json = data_example)
    return post_request
#bad

def perform_put_request():
    """Perform PUT request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/put'
    data = {'first_name': 'Guido','last_name': 'van Rossum'}
    put_request = requests.put ('https://httpbin.org/put', json = data)
    return put_request 
#bad

def perform_patch_request():
    """Perform PATCH request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/patch'
    data = {
        'first_name': 'Guido'
    }
    patch_request = requests.patch ('https://httpbin.org/patch', json = data)
    return patch_request
#bad

def perform_delete_request():
    """Perform DELETE request to given URL and return the response"""
    url = 'https://httpbin.org/delete'
    delete_request = requests.delete ('https://httpbin.org/delete')
    return delete_request
#ok

def perform_redirect_request():
    """Perform a request to a redirect URL and return the Location header that come in the response"""
    # HINT: you should use the allow_redirects parameter while doing the request
    url = 'https://httpbin.org/redirect/1'
    r = requests.get ('https://httpbin.org/redirect/1', allow_redirects = False)
    location = r.headers ['Location']
    return location
    
#bad
