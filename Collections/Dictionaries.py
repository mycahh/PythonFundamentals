Pokedex = {
    1: {
        "NAME": "BULBASAUR",
        "TYPE1": "GRASS",
        "TYPE2": "POISON",
    },
    2: {
        "NAME": "IVYSAUR",
        "TYPE1": "GRASS",
        "TYPE": "POISON"
    }
}

# Modify
Pokedex[1] = {
    "NAME": "BULBASAUR",
    "TYPE1": "GRASS",
    "TYPE2": "POISON",
    "GROWTH_RATE": "PARABOLIC"
}

# First Way to find
BULBASAUR = Pokedex[1]

print(BULBASAUR)

# Second Way to find
IVYSAUR = Pokedex.get(2)
print(IVYSAUR)

# Iter Dictionary
for key, value in Pokedex.items():
    print(f'No.{key} {value["NAME"]}')

# Check
BulbasaurInDex = 1 in Pokedex
print(BulbasaurInDex)


# Add 
Pokedex[3] = {
    "NAME": "VENASAUR",
    "TYPE1": "GRASS",
    "TYPE2": "POISON",
}

Pokedex.pop(1)

# Get keys
for key in Pokedex.keys():
    print(key)

# Get Values
for value in Pokedex.values():
    print(value)

# Clear
Pokedex.clear()

# Delete
del Pokedex