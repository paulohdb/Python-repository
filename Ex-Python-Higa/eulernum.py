def fat(x):
    fator = 1

    for j in range(1, x+1):

        fator = j * fator
    
    return fator

#===============================

def euler(n, m):
    eul = n ** 0
    x = 1

    while x <= m:
        
        eul = eul + ((n ** x) / fat(x))

        x += 1
    
    return eul

#===============================

def main():
    n = float(input())
    m = int(input())
    num = euler(n, m)
    print(f'{num:.4f}')

#===============================

main()