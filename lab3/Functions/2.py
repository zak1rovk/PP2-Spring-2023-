def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
x = fahrenheit_to_celsius(int(input()))
print(x)
