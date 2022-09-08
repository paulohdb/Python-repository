n = float(input())
m = int(input())

cons = 1
cont = 0
x = 2

while x <= m:
    fator = 1

    for j in range(1, x+1):
        fator = j * fator

    if cont % 2 == 0:
        cons = cons - ((n ** x) / fator)
    else:
        cons = cons + ((n ** x) / fator)

    cont += 1

    x += 2

print(f"{cons:.4f}")