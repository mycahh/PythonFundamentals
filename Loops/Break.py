str = "Hello Peter"

# OPTIONAL: else

pattern = "e"

for letter in str:
    if letter == pattern:
        print(f"{pattern} founded")
        break
else:
    print("Not founded")