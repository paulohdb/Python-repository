# -*- coding: utf-8 -*-

# lst_matriz = Criar uma lista vazia para a matriz
lst_matriz = []

# col = Ler a coluna em que a operação será realizada
col = int(input())

# op = Ler qual operação a ser realizada ('S' ou 'M')
op = input()

# para i de 0 a 11
for i in range(12):
    # lst_linha = Criar uma lista vazia para a linha
    lst_linha = []
    # para j de 0 a 11
    for j in range(12):
        # Ler um valor, convertê-lo para float
        # e inseri-lo em lst_linha
        lst_linha.append(float(input()))
    # Adicionar lst_linha à matriz lst_matriz
    lst_matriz.append(lst_linha)

# soma = 0.0
soma = 0.0

# para i de 0 a 11
for i in range(12):
    # soma += lst_matriz[i][col]
    soma += lst_matriz[i][col]

# se op == 'S'
if op == 'S':
    # Mostrar soma com 1 casa decimal
    print("{:.1f}".format(soma))
# senão
else:
    # Mostrar soma/12 com 1 casa decimal
    print("{:.1f}".format(soma/12))