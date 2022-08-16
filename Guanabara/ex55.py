maior = 0
menor = 0


for i in range(1, 6):

    peso = float(input())

    if i == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("Maior peso: Kg {}" .format(maior))
print("Menor peso: Kg {}" .format(menor))