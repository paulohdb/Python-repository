import random

n = int(input("Digite um número de 1 à 5: "))

ran = random.randint(0, 5)

if n == ran:
    
    print("Você acertou o número")

else:
    print("Você não acertou o número")