import requests

#Test for GET /orders
def test_get_orders_customer(base_url, user, password):
    s = requests.Session()
    s.auth = (user, password)
    s.headers.update({'x-test': 'true'})
    s.get('http://localhost/login', headers={'x-test2': 'true'})

    api = base_url + '/orders'
    expected_result = [{"customerId":"57a98d98e4b00679b4a830b2","customer":{"firstName":"User","lastName":"Name","username":"user","addresses":[],"cards":[]},"address":{"number":"246","street":"Whitelees Road","city":"Glasgow","postcode":"G67 3DL","country":"United Kingdom"},"card":{"longNum":"5544154011345918","expires":"08/19","ccv":"958"},"items":[{"itemId":"3395a43e-2d88-40de-b95f-e00e1502085b","quantity":1,"unitPrice":18}],"shipment":{"name":"57a98d98e4b00679b4a830b2"},"date":"2022-05-18T21:56:40.476+0000","total":22.99,"_links":{"self":{"href":"http://orders/orders/62856b9897a1c00008b9bedb"},"order":{"href":"http://orders/orders/62856b9897a1c00008b9bedb"}}}]
    expected_content_type = 'text/plain; charset=utf-8'
    response = s.get(api)
    response_body = response.json()
    response_header = response.headers
    assert response.status_code == 201, f'Error Code :{response.status_code}'
    assert response_body == expected_result, 'GET test_get_orders_customer - Failed'
    assert response_header["Content-Type"] == expected_content_type, 'GET test_get_orders_customer - Failed'

    customer_id = response_body[0]['customerId']
    api = base_url + f'/customers/{customer_id}'
    expected_result = {"firstName":"User","lastName":"Name","username":"user","id":"57a98d98e4b00679b4a830b2","_links":{"addresses":{"href":"http://user/customers/57a98d98e4b00679b4a830b2/addresses"},"cards":{"href":"http://user/customers/57a98d98e4b00679b4a830b2/cards"},"customer":{"href":"http://user/customers/57a98d98e4b00679b4a830b2"},"self":{"href":"http://user/customers/57a98d98e4b00679b4a830b2"}}}
    response = s.get(api)
    response_body = response.json()
    response_header = response.headers
    assert response.status_code == 200, f'Error Code :{response.status_code}'
    assert response_body == expected_result, 'GET test_get_orders_customer - Failed'
    assert response_header["Content-Type"] == expected_content_type, 'GET test_get_orders_customer - Failed'
    
    return


if __name__ == '__main__':
    base_url = 'http://localhost:80'
    user = 'user' 
    password = 'password'
    test_get_orders_customer(base_url, user, password)