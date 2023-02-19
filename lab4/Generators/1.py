n = int(input())
def gen_squares(n):
    for i in range(n):
        yield i**2
for x in gen_squares(n):
    print(x)