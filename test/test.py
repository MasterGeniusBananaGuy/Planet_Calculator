import json

saves = open('saves.json', 'r')
saves = saves.read()
planets = json.loads(saves)



print(str(planets))
