# NO ORDER. NO DUPLICITY VALUES.
Planets = {'Mars', 'Jupiter', 'Earth'}

# LENGTH
length = len(Planets)

# Check
EarthInPlanets = 'Earth' in Planets

# Add
Planets.add('Earth')

# Remove (THROW A POSSIBLE ERROR)
Planets.remove('Jupiter')

# Remove (NO THROW A POSSIBLE ERROR)
Planets.discard('Jupiter')

print(EarthInPlanets)
print(Planets)

# Clear the Set
Planets.clear()

# Delete Set
del Planets