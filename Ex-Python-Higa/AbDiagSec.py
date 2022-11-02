def verifica(question: str, matriz: list, p: int):

    soma = media = cont = con = 0

    oi = 1

    if question == "S":

        for i in range(p-1, 1, -1):

            for j in range(oi, 12):

                soma += matriz[i][j]

        oi += 1
        
        return soma

    else:

        for i in range(p-1, 0, -1):

            for j in range(oi, 12):

                media += matriz[i][j]

                con += 1
            
            oi += 1

        cont = media / con

        return cont
            
            

def main():

    q = input()

    p = 12

    M = [[0] * p for i in range(p)]

    for i in range(p):

        for j in range(p):

            M[i][j] = float(input())

    value = verifica(q, M, p)

    print(f'{value:.1f}')

main()           