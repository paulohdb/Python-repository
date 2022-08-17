# -*- coding: utf-8 -*-

# maior = Ler número inteiro
maior = int(input())
# posmaior = 1
posmaior = 1

# para i de 2 a 100
for i in range(2, 101):
    # n = Ler número inteiro
    n = int(input())
    # se n > maior
    if n > maior:
        # então maior = n
        #       posmaior = i
        maior = n
        posmaior = i
# Mostrar maior
print(maior)
# Mostrar posmaior
print(posmaior)