import requests

pokemon = input("Enter the Pokemon name:  ")
pokemon = pokemon.lower()

dynamicURL = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

req = requests.get(dynamicURL)
pokemonData = req.json()

print("\n","Name is:  ", pokemonData['name'], "\n")

print ("ABILITIES: ", "\n")
for ability in pokemonData['abilities']:
    print(ability['ability']['name'], "\n")

print ("More about ABILITIES: ", "\n")
for ability in pokemonData['abilities']:
    print(ability['ability']['url'], "\n")

print ("More about GAME INDICES: ", "\n")
for indices in pokemonData['game_indices']:
    print("Game index:  ",indices['game_index'], "\n")
    print("Version name: ", indices['version']['name'], "\n")
    print("More on Version: ", indices['version']['url'], "\n")







