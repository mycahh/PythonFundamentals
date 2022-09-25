Cities = ['Accumula', 'Black', 'Castelia', 'Dewford', 'Ecruteak']

### print(names[0]) # Alice
### print(names[-1]) # Ecruteak

print(Cities[:2]) 
print(Cities[1:])
print(Cities[1:4])

length = len(Cities) # To know the Length of the List
print(length)

Cities.append('Floccesy') # Added (Last)
Cities.insert(0,'Agate') # Add (Specific Index)
Cities.pop() # Last (Default) 

CasteliaInCities = 'Castelia' in Cities
print(CasteliaInCities)

Cities.clear() # Clear the List

### del Cities # Delete

print(Cities)

# for City in Cities:
#    print(City)