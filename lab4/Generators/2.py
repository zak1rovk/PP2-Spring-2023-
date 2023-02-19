def gen_alleven():
    n = 0
    while True :
        yield n
        n += 2
print(gen_alleven())