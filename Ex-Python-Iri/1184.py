# -*- coding: utf-8 -*-

# lst_matriz = Criar uma lista vazia para a matriz
lst_matriz = []

# op = Ler a operação a ser realizada ('S' ou 'M')
op = input()

# para i de 0 a 11
for i in range(12):
    # lst = Criar lista vazia para a linha
    lst = []
    # para j de 0 a 11
    for j in range(12):
        # Ler o valor, convertê-lo para float
        # e atribuí-lo à lista lst
        lst.append(float(input()))
    # Colocar a linha lst na matriz lst_matriz
    lst_matriz.append(lst)

# Contador n para a quantidade de elementos de interesse
n = 0

# Variável soma para armazenar a soma dos
# elementos de interesse
soma = 0.0

# para i de 1 a 11
for i in range(1, 12):
    # para j de 0 a i-1
    for j in range(0, i):
        soma += lst_matriz[i][j]
        n += 1
    # n += i
        
# se op == 'S'
if op == 'S':
    # Mostrar soma com 1 casa decimal
    print("{0:.1f}".format(soma))
# senão
else:
    # Mostrar soma/n com 1 casa decimal
    print("{0:.1f}".format(soma/n))
