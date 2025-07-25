import requests


key2 = "01440335f494948746f8b12538791c0a"
api_address = f"http://api.openweathermap.org/data/2.5/weather?q=Tumakuru&appid={key2}"
json_data = requests.get(api_address).json()

def temp():
        temperature = round(json_data["main"]["temp"] - 273.15, 1)
        return temperature

def des():
        description = json_data["weather"][0]["description"]
        return description

