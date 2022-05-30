# from urllib import response
import requests

def test_register_user(base_url):
    api = base_url + '/register'
    payload = {
                "username": "sockshoptestuser",
                "password": "sockshop@123",
                "email": "sockshoptestuser@gmail.com"
              }
    
    response = requests.post(api, data=payload)
    print(response.text) 

def test_carts(base_url):
    api = base_url + '/carts'
    response = requests.get(api)
    print(response.status_code)


def test_login_orders(base_url):
    api = base_url + '/login'
    response = requests.get(api)
    print(response.status_code)
    print(response.text)

if __name__ == '__main__':
    base_url = 'http://localhost:80'
    # user = 'user'
    # password = 'password'

    # test_register_user(base_url)
    # test_carts(base_url)
    test_login_orders(base_url)
