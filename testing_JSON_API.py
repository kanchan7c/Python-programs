import requests

req = requests.get("https://dog.ceo/api/breeds/image/random")
dog = req.json()

print(dog['message'])