"""
    A ideia do problema é fazer um algoritimo que irá ler primeiro 
    um valor de caso de testes N, que definirá quantas vezes testaremos o
    algoritimo.

    Cada caso de teste, terá 6 linhas de input, cada 3 linhas, é uma pessoa diferente.

    Cada linha do input terá dois valores inteiros que é o X e D, onde X computa
    a pontuação, e D (segundo valor) é a pontuação da distancia.

    Na saida, teremos apenas o vencedor printado de cada caso de teste
"""

n = int(input())

pointJ = 0

pointM = 0

for i in range(n):

    for i in range(3):

        xjint, djint = input().split()

        xj = int(xjint)
        dj = int(djint)

        totalJ = xj * dj

        pointJ = pointJ + totalJ

    for i in range(3):

        xmint, dmint = input().split()

        xm = int(xmint)
        dm = int(dmint)

        totalM = xm * dm

        pointM = pointM + totalM

    if pointM > pointJ:
        print("MARIA")

    else:
        print("JOAO")

    