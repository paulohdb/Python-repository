
def verifica(line: int, question: str, matriz: list):

    soma = media = cont = 0

    if question == "S":

        for i in range(12):

            soma += matriz[line][i]
        
        return soma

    else:

        for i in range(12):

            media += matriz[line][i]

            cont = media / 12

        return cont
            
            

def main():

    line = int(input())

    q = input()

    M = [[0] * 12 for i in range(12)]

    for i in range(12):

        for j in range(12):

            M[i][j] = float(input())

    value = verifica(line, q, M)

    print(value)

main()           