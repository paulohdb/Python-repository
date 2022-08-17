# -*- coding: utf-8 -*-

# A ideia é fazer um laço com término indefinido.
# Em cada repetição do laço, primeiro ler o número inteiro n e
# verificar se ele é zero. Se n for zero, sair do laço.
# Caso contrário, verificar se ele é par. Se n é par,
# já consideramos n como primeiro par da soma.
# Se n for ímpar, somamos 1 para encontrar o primeiro par da soma.
# Fazemos então outro laço para fazer as quatro somas necessárias
# para obter o resultado, e o mostramos.

# Enquanto Verdadeiro
while True:
    # n = Ler inteiro
    n = int(input())
    # se n == 0
    if n == 0:
        # Sair do laço enquanto
        break
    # se n é par
    if n % 2 == 0:
        # então inicio = n
        inicio = n
        # senão inicio = n + 1
    else:
        inicio = n + 1
    # soma = inicio
    soma = inicio
    # para i de 1 a 4
    for i in range(4):
        # inicio = inicio + 2
        inicio = inicio + 2
        # soma = soma + inicio
        soma = soma + inicio
    # Mostrar soma
    print(soma)