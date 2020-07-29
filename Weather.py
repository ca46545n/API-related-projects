from pprint import pprint
import requests

r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Jersey City&appid=28b3b190099f4f80bf640a1673190eb1")
weather1 = r.json()
weather = weather1['weather']
city = weather1['name']
print('Location:', city)
print('Weather:',weather)

