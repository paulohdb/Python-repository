from random import randint

comp = randint(0, 10)

print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adviinhar qual foi?")

acertou = False
palp = 0

while not acertou:

    jogador = int(input("Qual o seu palpite? "))
    palp += 1

    if jogador == comp:
        acertou = True

    else:

        if jogador < comp:
            print("Mais... Tente de novo")

        elif jogador > comp:
            print("Menos... Tente de novo")    

print("Acertou com {} tentativas" .format(palp))