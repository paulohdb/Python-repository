tup = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez")

while True:
    num = int(input())

    if 0 <= num <= 10:
        break

    print("Tente novamente. ", end="")

print("Você digitou o número {}" .format(tup[num]))