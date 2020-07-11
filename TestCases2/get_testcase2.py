import requests, json, jsonpath

base_url = "https://reqres.in/api/users?page=2"
response = requests.get(base_url) 

json_response = json.loads(response.text)
pages = jsonpath.jsonpath(json_response,'total_pages')
assert pages[0] == 2,"Page should be 2"

# Checking for GET Assertion error
assert response.status_code == 200
x = response.json()
print(x)
print("You Succesfully got the data")
