from Person import Person, PersonOnlyRead

NPC2 = Person('Daniel')
NPC3 = PersonOnlyRead('Peter')

NPC2.name = 'Haro'
# NPC3.name = 'Malon' ## ERROR ##

print(NPC2.name)