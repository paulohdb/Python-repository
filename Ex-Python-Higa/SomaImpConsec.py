def verifica(X, Y: int):
    if X < Y:
        start = X
        final = Y
    else:
        start = Y
        final = X

    if start % 2 != 0:
        start = start + 2
    else:
        start = start + 1

    if final % 2 != 0:
        final = final - 2
    else:
        final = final - 1
    
    return start, final

#===================================

def main():

    X = int(input())
    Y = int(input())

    if X == Y:
        print(0)

    else:

        sta, fin = verifica(X, Y)
        
        soma = 0

        for i in range(sta, fin+1, 2):
            
            soma = soma + i
        
        print(soma)

#===================================

main()
