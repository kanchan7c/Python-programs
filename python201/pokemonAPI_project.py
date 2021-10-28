import requests

while True:
    pokemon = input("Enter the Pokemon name:  ")
    pokemon = pokemon.lower()

    dynamicURL = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    req = requests.get(dynamicURL)

    if req.status_code == 200:
        pokemonData = req.json()

        print("\n","Name is:  ", pokemonData['name'], "\n")

        print ("ABILITIES: ", "\n")
        for ability in pokemonData['abilities']:
            print(ability['ability']['name'], "\n")

        print ("More about ABILITIES: ", "\n")
        for ability in pokemonData['abilities']:
            print(ability['ability']['url'], "\n")

    else: 
        print(f"'{pokemon}' is not a valid pokemon name")






