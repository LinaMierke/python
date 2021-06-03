v = [1, 3, 5, 7, 90, 67, 29, 19, 17, 3, 1, 2, 5, 6, 7, 8]
pares = []
impares = []
menos10 = []
divisibles = []


def prime_num(v):
    primos = []
    for i in v:
        if i > 1:
            if i == 2 or i == 3:
                primos.append(i)
            if i % 2 == 0 or i % 3 == 0:
                divisibles.append(i)
            else:
                primos.append(i)
    return primos


print(prime_num(v))
