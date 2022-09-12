dec = int(input())

exp = bi = 0

while dec != 0:

    r = dec % 2
    dec = dec // 2

    bi = bi + r * (10 ** exp)

    exp += 1

print(bi)