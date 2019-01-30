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
    
    response = requests.get(url, params={'any_param': 'test'}) #new
    return response

# r = requests.post('https://httpbin.org/post', data = {'key':'value'})
# Troy: How do I know the keywords is json?
def perform_post_request():
    """Perform POST request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/post'
    data = {
        'first_name': 'Guido',
        'last_name': 'van Rossum'
    }
    
    response = requests.post(url, json = data) # 405 response?
    return response

# Troy: again how do I know this is JSON
def perform_put_request():
    """Perform PUT request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/put'
    data = {
        'first_name': 'Guido',
        'last_name': 'van Rossum'
    }
    response = requests.put(url, json = data)
    return response


def perform_patch_request():
    """Perform PATCH request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/patch'
    data = {
        'first_name': 'Guido'
    }
    response = requests.patch(url, json = data)
    return response


def perform_delete_request():
    """Perform DELETE request to given URL and return the response"""
    url = 'https://httpbin.org/delete'
    
    response = requests.delete(url)
    return response


def perform_redirect_request():
    """Perform a request to a redirect URL and return the Location header that come in the response"""
    # HINT: you should use the allow_redirects parameter while doing the request
    url = 'https://httpbin.org/redirect/1'
    
    response = requests.get(url, allow_redirects=False)
    return response.headers['Location']

    # Troy: How do I know what headers can be returned?


## TROY: QUESTIONS BELOW

# def perform_get_request_with_params():
#     """Perform GET request to given URL sending any parameter and return the response"""
#     # HINT: you should add the GET parameters at the end of the url
#     url = 'https://httpbin.org/get'
#     response = requests.get(url) #new
#     return response

# hard to enderstand error
# E       AssertionError: assert False
# E        +  where False = <built-in method startswith of str object at 0x7f240e489738>('https://httpbin.org/get?')
# E        +    where <built-in method startswith of str object at 0x7f240e489738> = 'https://httpbin.org/get'.startswith
# E        +      where 'https://httpbin.org/get' = <PreparedRequest [GET]>.url
# E        +        where <PreparedRequest [GET]> = <Response [200]>.request