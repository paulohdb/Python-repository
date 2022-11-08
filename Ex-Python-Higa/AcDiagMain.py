def verifica(matriz: list, p: int):

    soma = con = 0

    for i in range(p):

        oi = 12

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

    value, conta = verifica(M, p)

    if q == "S":
        print(f'{value:.1f}')
    else:
        print(f'{value/conta:.1f}')

main()           