def convert_grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
x = convert_grams_to_ounces(float(input()))
print(x)