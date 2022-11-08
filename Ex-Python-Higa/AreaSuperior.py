def verifica(matriz: list):

    soma = con = 0

    oi = 11

    for i in range(5):

        for j in range(i+1, oi):

            soma += matriz[i][j]
            con += 1

        oi -= 1
    
    return soma, con

def main():

    q = input()

    p = 12

    M = [[0] * p for i in range(p)]

    for i in range(p):

        for j in range(p):

            M[i][j] = float(input())

    value, conta = verifica(M)

    if q == "S":
        print(f'{value:.1f}')
    else:
        print(f'{value/conta:.1f}')

main()           