import requests

#Test for GET /customers
def test_get_customers(base_url):
    api = base_url + '/customers'
    expected_result = {"_embedded":{"customer":[{"firstName":"Eve","lastName":"Berger","username":"Eve_Berger","id":"57a98d98e4b00679b4a830af",
    "_links":{"addresses":{"href":"http://user/customers/57a98d98e4b00679b4a830af/addresses"},"cards":{"href":"http://user/customers/57a98d98e4b00679b4a830af/cards"},
    "customer":{"href":"http://user/customers/57a98d98e4b00679b4a830af"},"self":{"href":"http://user/customers/57a98d98e4b00679b4a830af"}}},
    {"firstName":"User","lastName":"Name","username":"user","id":"57a98d98e4b00679b4a830b2","_links":{"addresses":{"href":"http://user/customers/57a98d98e4b00679b4a830b2/addresses"},"cards":{"href":"http://user/customers/57a98d98e4b00679b4a830b2/cards"},"customer":{"href":"http://user/customers/57a98d98e4b00679b4a830b2"},"self":{"href":"http://user/customers/57a98d98e4b00679b4a830b2"}}},{"firstName":"User1","lastName":"Name1","username":"user1","id":"57a98d98e4b00679b4a830b5","_links":{"addresses":{"href":"http://user/customers/57a98d98e4b00679b4a830b5/addresses"},"cards":{"href":"http://user/customers/57a98d98e4b00679b4a830b5/cards"},"customer":{"href":"http://user/customers/57a98d98e4b00679b4a830b5"},"self":{"href":"http://user/customers/57a98d98e4b00679b4a830b5"}}}]}}
    expected_content_type = 'text/plain; charset=utf-8'
    response = requests.get(api)
    assert response.status_code == 200, f'Error {response.status_code}'
    response_body = response.json()
    response_header = response.headers
    assert response_body == expected_result, 'GET /customers - Failed'
    assert response_header["Content-Type"] == expected_content_type, 'GET /customers - Failed'
    # print('test_get_customers - Passed')
    return

#Test for GET /cards/{id}
def test_get_cards_id(base_url, id):
    api = base_url + '/cards/' + id
    expected_result = {"longNum":"5953580604169678","expires":"08/19","ccv":"678","id":"57a98d98e4b00679b4a830ae","_links":{"card":{"href":"http://user/cards/57a98d98e4b00679b4a830ae"},"self":{"href":"http://user/cards/57a98d98e4b00679b4a830ae"}}}
    expected_content_type = 'text/plain; charset=utf-8'
    response = requests.get(api)
    assert response.status_code == 200, f'Error {response.status_code}'
    response_body = response.json()
    response_header = response.headers
    assert response_body == expected_result, 'GET /cards/id - Failed'
    assert response_header["Content-Type"] == expected_content_type, 'GET /cards/id - Failed'
    # print('test_get_cards_id - Passed')
    return

#Test for GET /cards/{id} Error
def test_get_cards_id_error(base_url, id):
    api = base_url + '/cards/' + id
    expected_result = {"error":"Do: Invalid Id Hex","status_code":500,"status_text":"Internal Server Error"}
    response = requests.get(api)
    response_body = response.json()
    assert response_body == expected_result, 'GET /cards - Failed'
    return

#Test for GET /catalogue/{id}
def test_get_catalogue_id(base_url, id):
    api = base_url + '/catalogue/' + id
    expected_result = {"id":"a0a4f044-b040-410d-8ead-4de0446aec7e","name":"Nerd leg","description":"For all those leg lovers out there. A perfect example of a swivel chair trained calf. Meticulously trained on a diet of sitting and Pina Coladas. Phwarr...","imageUrl":["/catalogue/images/bit_of_leg_1.jpeg","/catalogue/images/bit_of_leg_2.jpeg"],"price":7.99,"count":115,"tag":["blue","skin"]}    
    expected_content_type = 'text/plain; charset=utf-8'
    response = requests.get(api)
    assert response.status_code == 200, f'Error {response.status_code}'
    response_body = response.json()
    response_header = response.headers
    assert response_body == expected_result, 'GET /catalogue/id - Failed'
    assert response_header["Content-Type"] == expected_content_type, 'GET /catalogue/id - Failed'
    # print('test_get_catalogue_id - Passed')
    return

#Test for GET /catalogue/{id} Error
def test_get_catalogue_id_error(base_url, id):
    api = base_url + '/catalogue/' + id
    expected_result = {"error":"Do: not found","status_code":500,"status_text":"Internal Server Error"}
    response = requests.get(api)
    response_body = response.json()
    assert response_body == expected_result, 'GET /catalogue - Failed'
    return



if __name__ == '__main__':
    base_url = 'http://localhost:80'
    test_get_customers(base_url)
    test_get_cards_id(base_url, '57a98d98e4b00679b4a830ae')
    test_get_cards_id_error(base_url, 'test')
    test_get_catalogue_id(base_url, 'a0a4f044-b040-410d-8ead-4de0446aec7e')
    test_get_catalogue_id_error(base_url, 'test')
    
