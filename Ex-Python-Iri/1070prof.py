# -*- coding: utf-8 -*-

# n = Ler número inteiro
n = int(input())

# se n for par
if n % 2 == 0:
    # então impar = n + 1
    impar = n + 1
# senão
else:
    # impar = n
    impar = n
    
# para i de 1 a 6
for i in range(6):
    # Mostrar impar
    print(impar)
    # impar = impar + 2
    impar = impar + 2