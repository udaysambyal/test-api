# test-api
Refer to Document.docx
 or

API rest framework Testing
Command: - pytest     		 (For running both the test cases at a time.)
I have made two Test cases: 
1.	Testcases1: 
I have used open source weather API (https://openweathermap.org/). I have fetched the data from this open source weather API by using GET request and API Key. It has two files : 
•	get_testcase1.py:- Run this file for output. (Command:- python get_testcase1.py). It has 2 validations: 
	status code validation for checking status code = 200
	Content type header validation for checking the type of file.
•	test_get1.py:- Run this file for testing individually. (Command:- pytest)
2.	Testcases2:
I have used open source Regres API (https://reqres.in/api/users?page=2). I have used three different types of request in it i.e. (GET, POST, and DELETE). It has 4 files:
•	get_testcase2.py:- Run this file for output. (Command:- python get_testcase2.py). It has 2 validations: 
	status code validation for checking status code = 200
	Page checking validation to check weather on the right page or not.
•	post_testcase2.py:- Run this file for output. (Command:- python get_testcase2.py). It has 1 validation: 
	status code validation for checking status code of post = 201
•	delete_testcase2.py:- Run this file for output. (Command:- python get_testcase2.py). It has 1 validation: 
	status code validation for checking status code of delete = 204
•	get_all.py:- Run this file for testing individually. (Command:- pytest)
