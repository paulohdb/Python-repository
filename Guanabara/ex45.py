from math import radians
from random import randint

itens = ("Pedra", "Papel", "Tesoura")

comp = randint(0, 2)

print("""Sua opções:

0 - Pedra
1 - Papel
2 - Tesoura""")

player = int(input("Qual a sua jogada? "))

print("Computador jogou {}" .format(itens[comp]))

print("Jogador jogou {}" .format(itens[player]))

if comp == 0:

    if player == 0:
        print("Empate")
    elif player == 1:
        print("Jogador Vence")
    elif player == 2:
        print("Computador Vence")
    else:
        print("JOGADA INVÁLIDA!")

elif comp == 1:

    if player == 0:
        print("Computador Vence")
    elif player == 1:
        print("Empate")
    elif player == 2:
        print("Jogador vence")
    else:
        print("JOGADA INVÁLIDA!")


elif comp == 2:

    if player == 0:
        print("jogador Vence")
    elif player == 1:
        print("Computador Vence")
    elif player == 2:
        print("Empate")
    else:
        print("JOGADA INVÁLIDA!")
