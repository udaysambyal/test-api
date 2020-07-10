# Python program to find current  
# weather details of any city 
# using openweathermap api 

import requests, json 

api_key = "1b9f70d18e7dbf72599a5682c9e05a75"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=delhi"  

def  test_for_get():
    response = requests.get(complete_url) 

    # Checking for GET Assertion error
    assert response.status_code == 200
    x = response.json() 

    # assertion for Content type header
    contentType = response.headers['Content-Type']
    assert contentType == "application/json; charset=utf-8","Content type is application/json"

    if x["cod"] != "404": 
        current_temperature = x["main"]["temp"] 
        current_pressure = x["main"]["pressure"] 
        current_humidiy = x["main"]["humidity"] 
        weather_description = x["weather"][0]["description"] 
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description))  
    else: 
        print(" City Not Found ") 

