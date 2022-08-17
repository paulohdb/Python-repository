'''
    PROBLEMA DE NÚMERO 2031 - PEDRA, PAPEL, ATAQUE AÉREO

    O código lerá um primeiro número para dizer quantas vezes
    o código irá rodar dentro de um for, o caso de testes.

    Faremos um for i até n, depois, dois inputs, respectivamente
    jogador um sendo o primiero input da primeira linha, e o segundo input
    sendo o segundo jogador.

    Em seguida, terá todas as comparações e possibilidades entre os jogadores,
    se caso o jogador 1 venca, se caso o jogador 2 vença, se caso os dois ganhem, ou se caso
    os dois jogadores percam ou até se não ter jogador com vitória.

    Em cada linha de comparação, terá uma linha de imprimir embaixo delas, imprimindo o resultado
    se caso aquela linha de comparação teve exito.
'''


# Ler um valor inteiro n
n = int(input())

# para i até n
for i in range(n):


    # Ler duas strings em duas linhas diferentes
    jog1 = input()

    jog2 = input()

    #
    
    # Se o jogador 1 for ataque e o jogador 2 for pedra
    if jog1 == "ataque" and jog2 == "pedra":
        # imprimir o jogador 1 venceu
        print("Jogador 1 venceu")

    # senão, jogador um for pedra e jogador dois for ataque
    elif jog1 == "pedra" and jog2 == "ataque":
        # imprimir o jogador 2 venceu
        print("Jogador 2 venceu")

    #
    # senão, jogador um for pedra e jogador dois for papel
    elif jog1 == "pedra" and jog2 == "papel":
        # imprimir o jogador 1 venceu
        print("Jogador 1 venceu")

    # senão, jogador 1 for papel e jogador dois for pedra
    elif jog1 == "papel" and jog2 == "pedra":
                # imprimir o jogador 2 venceu
        print("Jogador 2 venceu")

    #

    # senão, jogador 1 for papel e jogador for ataque
    elif jog1 == "papel" and jog2 == "ataque":
                # imprimir o jogador 2 venceu
        print("Jogador 2 venceu")
    
    #senão, jogador um for ataque e jogador dois for papel
    elif jog1 == "ataque" and jog2 == "papel":
        # imprimir o jogador 1 venceu
        print("Jogador 1 venceu")

    #

    # senão, jogador um for pedra e jogador dois for pedra
    elif jog1 == "pedra" and jog2 == "pedra":
        # imprimir Sem ganhador
        print("Sem ganhador")

    #

    #senão jogador 1 for papel e jogador dois for papel
    elif jog1 == "papel" and jog2 == "papel":
    # imprimir Ambos venceram
        print("Ambos venceram")

    #

    # jogador um for ataque e jogador dois for ataque
    elif jog1 == "ataque" and jog2 == "ataque":
        # imprimir Aniquilação mutua
        print("Aniquilacao mutua")
