import requests

api_key = "b4b861b7fc9b4e058ea201654252607"
city = "Nairobi"
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"


response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    location = data['location']['name']
    temp = data['current']['temp_c']
    condition = data['current']['condition']['text']
    print(f"Weather in {location}")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {condition}")
else:
    print("Failed to retrieve weather data.") 