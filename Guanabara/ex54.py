from datetime import date

atual = date.today().year

maior = 0
menor = 0

for i in range(1, 8):

    nasc = int(input())

    idade = atual - nasc

    if idade >= 21:
        
        maior += 1

    else:

        menor += 1

print("Tivemos {} pessoas menores de idade" .format(menor))

print("Tivemos {} pessoas maiores de idade" .format(maior))