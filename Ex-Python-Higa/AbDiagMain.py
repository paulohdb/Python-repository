def verifica(question: str, matriz: list, p: int):

    soma = media = cont = con = 0

    if question == "S":

        for i in range(1, p):

            for j in range(i):

                soma += matriz[i][j]

        
        return soma

    else:

        for i in range(1, p):

            for j in range(i):

                media += matriz[i][j]
                
                con += 1

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