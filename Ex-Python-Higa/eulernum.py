n = float(input())
m = int(input())

eul = n ** 0
x = 1

while x <= m:
    fator = 1

    for j in range(1, x+1):
        fator = j * fator

    eul = eul + ((n ** x) / fator)

    x += 1

print(f'{eul:.4f}')