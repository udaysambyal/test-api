import requests, json, jsonpath

base_url = "https://reqres.in/api/users?page=2"
response = requests.delete(base_url)


# Checking for Delete Assertion error
assert response.status_code == 204,"Assertion delete"
print("Sucessfully Deleted")
