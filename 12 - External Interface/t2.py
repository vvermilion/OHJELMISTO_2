import requests
#
city = input("Enter city: ")
api_key = "ab6df88555bc7505c44255eddf688db1"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
#
response = requests.get(url)
data = response.json()
#
description = data["weather"][0]["description"]
#
kelvin_temp = data["main"]["temp"]
celsius_temp = kelvin_temp - 273.15
#
print(f"The weather in {city} is: {description}")
print(f"Temperature: {celsius_temp:.1f}°C")