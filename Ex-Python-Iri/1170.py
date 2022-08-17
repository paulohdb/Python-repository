n = int(input())

for i in range(n):

    c = float(input())

    dias = 0

    while c > 1.0:
        dias += 1

        c /= 2
    
    print("{} dias" .format(dias))