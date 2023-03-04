import string
for letter in string.ascii_uppercase:
    file_path = letter + ".txt"
    with open(file_path, "w") as file:
        pass
