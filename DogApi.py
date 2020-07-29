import random
import requests
import json
Dog = requests.get("https://dog.ceo/api/breeds/list/all")
Dog1 = Dog.json()
Dogs = Dog1['message']
t = key, val = random.choice(list(Dogs.items()))
b = list(t)
if len(val) == 0:
    b.insert(1,'Sorry no information on this breed as of yet.')
    b.pop()
print('Your random Dog choice is : ', str(b))

