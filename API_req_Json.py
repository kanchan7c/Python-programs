import requests

req = requests.get("https://swapi.dev/api/people/1")
person = req.json()
# print(person)
print(f"Name is \t \t{person['name']}")
print(f"Birth year is \t \t{person['birth_year']}")
print(f"Movies are \t \t{person['films']} \n")

for film in person['films']:
    req = requests.get(film)
    film = req.json()
    print("Film is:  ", film['title'],"\n")
