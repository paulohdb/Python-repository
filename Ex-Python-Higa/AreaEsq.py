def verifica(matriz: list, p: int):

    soma = con = 0

    oi = 0
    io = p - 1

    for i in range(oi, 5):

        for j in range(i+1, io):

            soma += matriz[j][i]
            con += 1
            
        oi += 1
        io -= 1
    
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