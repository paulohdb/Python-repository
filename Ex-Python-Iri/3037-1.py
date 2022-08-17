"""
    A ideia do problema é fazer um algoritimo que irá ler primeiro 
    um valor de caso de testes N, que definirá quantas vezes testaremos o
    algoritimo.

    Cada caso de teste, terá 6 linhas de input, cada 3 linhas, é uma pessoa diferente.

    Cada linha do input terá dois valores inteiros que é o X e D, onde X computa
    a pontuação, e D (segundo valor) é a pontuação da distancia.

    Teremos um for para cada n, sendo n o valor de quantas vezes irá ter 
    o lançamento de dardos.

    Dentro desse for, teremos outro for até 3 vezes, um representando a
    tentativa do primeiro e do segundo jogador.

    Por fim, teremos uma comparação de pontos dentre pointJ e pointM para
    termos a print de quem ganhou.
"""

# Ler um valor inteiro n
n = int(input())


# para cada i até n 
for i in range(n):

    # Declarar variáveis vazias para armazenar
    # o valor somado das pontuações

    # pointJ recebe 0
    pointJ = 0

    # pointM recebe 0
    pointM = 0


    # para i até 3
    for i in range(3):

        # Ler dois valores splitados
        xjint, djint = input().split()

        # xj recebe inteiro
        xj = int(xjint)
        # dj recebe inteiro
        dj = int(djint)

        # Variável totalJ receberá o valor de xj e dj, multiplicando
        # para se obter o valor total da pontuação.
        totalJ = xj * dj

        # Concatenação de pointJ para armazenar os valores.
        pointJ = pointJ + totalJ

    # para i até 3
    for i in range(3):

        # Ler dois valores splitados
        xmint, dmint = input().split()

        # xm recebe inteiro
        xm = int(xmint)

        # dm recebe inteiro
        dm = int(dmint)

        # Variável totalJ receberá o valor de xm e dm, multiplicando
        # para se obter o valor total da pontuação.
        totalM = xm * dm

        # Concatenação de pointM para armazenar os valores.
        pointM = pointM + totalM


    # Se pointM for maior que pointJ
    if pointM > pointJ:
        # Então, imprimir "MARIA"
        print("MARIA")
    # Senão
    else:
        # Imprimir "JOAO"
        print("JOAO")