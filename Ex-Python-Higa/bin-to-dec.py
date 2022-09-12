n = int(input())

dec = exp = 0

while n > 0:

    r = n % 10
    n = n // 10

    dec = dec + r * (2 ** exp)

    exp += 1

print(dec)