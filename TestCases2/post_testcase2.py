import requests, json ,jsonpath

base_url = "https://reqres.in/api/users?page=2"
f = open('file.json')
json_input = f.read()
request_json = json.loads(json_input)

response = requests.post(base_url,request_json)
# Checking for POST Assertion error
assert response.status_code == 201
response_json = json.loads(response.text)
id = jsonpath.jsonpath(response_json,'id')
print("Is is: ", id[0])
print("Successfully created")