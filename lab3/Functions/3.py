def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None
x = int(input())
y = int(input())
print(x)