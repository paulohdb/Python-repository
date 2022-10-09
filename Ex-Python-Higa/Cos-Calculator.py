def main():
    n = float(input())
    m = int(input())
    cos = calculaCos(n, m)
    print(f"{cos:.4f}")

#======================================

def fat(x):
    fator = 1

    for j in range(1, x+1):
        fator = j * fator
    
    return fator

#======================================

def calculaCos(n, m):
    cons = 1
    cont = 0
    x = 2

    while x <= m:
        
        if cont % 2 == 0:
            cons = cons - ((n ** x) / fat(x))
        else:
            cons = cons + ((n ** x) / fat(x))

        cont += 1

        x += 2
    
    return cons

#======================================

main()