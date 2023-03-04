string = "This is a Sample String"
num_upper = 0
num_lower = 0
for char in string:
    if char.isupper():
        num_upper += 1
    elif char.islower():
        num_lower += 1
print("Number of uppercase letters:", num_upper)
print("Number of lowercase letters:", num_lower)
