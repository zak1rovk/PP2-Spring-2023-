from math import tan, pi
num_sides = int(input())
side_length = int(input())
poly_area = num_sides * (side_length ** 2 ) / (4 * tan(pi / num_sides))
print(poly_area)