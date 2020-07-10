import requests, json, jsonpath

base_url = "https://reqres.in/api/users?page=2"  

def  test_for_get():
    
    response = requests.get(base_url) 
    json_response = json.loads(response.text)
    pages = jsonpath.jsonpath(json_response,'total_pages')
    assert pages[0] == 2

    # Checking for GET Assertion error
    assert response.status_code == 200
    

def test_for_delete():
    response = requests.delete(base_url)

    # Checking for Delete Assertion error
    assert response.status_code == 204,"Assertion delete"
    

def test_for_post():
    f = open('file.json')
    json_input = f.read()
    request_json = json.loads(json_input)

    response = requests.post(base_url,request_json)

    # Checking for POST Assertion error
    assert response.status_code == 201

    response_json = json.loads(response.text)

    id = jsonpath.jsonpath(response_json,'id')

    print(id[0])