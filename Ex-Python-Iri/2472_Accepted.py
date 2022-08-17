# -*- coding: utf-8 -*-

"""
    2472 - Interseção de vetores
    Seu programa deverá ler dois vetores de números inteiros,
    informar se há interseção entre os dois vetores e mostrar
    os valores de interseção se existirem. Assuma que não há valores
    repetidos dentro de cada vetor lido. O vetor que servirá para
    mostrar os elementos de interseção deve ter apenas a quantidade
    exata de posições correspondente aos valores que aparecem
    simultaneamente nos dois vetores lidos.

    Entrada:
    Ler o tamanho T1 do primeiro vetor V1 em uma linha e ler o
    vetor na segunda linha, com os valores inteiros separados
    por espaços. Ler o tamanho T2 do segundo vetor V2 em uma
    terceira linha e ler o vetor na quarta linha, com os valores
    inteiros separados por espaços. 
    
    Saída:
    Quando não houver valor que esteja
    simultaneamente nos dois vetores lidos, mostrar
    "Não há interseção!", Caso contrário, mostrar
    "Elementos de interseção:" em uma linha e
    na outra linha, o vetor gerado, elemento a elemento
    separados por espaço e sem espaço após o último elemento.
    
    Exemplos de entrada:           Exemplos de saída:
    4                              Elementos de interseção:
    10 30 50 100                   30 100
    3
    100 30 1

    5                              Não há interseção!
    -7 1 0 -6 100
    7
    -5 2 3 4 5 99 101
"""

"""
    A ideia geral, após ler o tamanho do primeiro vetor
    de inteiros T1, gerar o primeiro vetor de inteiros
    V1 a partir de uma lista de strings gerada por
    input().split(), ler o tamanho do segundo vetor de
    inteiros T2, gerar o segundo vetor de inteiros
    V2 a partir de uma lista de strings gerada por
    input().split(); compara-se T1 e T2 e o menor valor
    entre eles é atribuído à variável n; cria-se um
    vetor pre_inter de n inteiros, para armazenar, no
    máximo, n valores de interseção; utiliza-se uma
    variável ind_inter, inicialmente 0, como índice de
    pre_inter e como quantidade de elementos de interseção;
    via dois laços de repetição para, procura-se cada
    elemento de V1 em V2 e se encontra um, coloca-o em
    pre_inter e incrementa ind_inter de uma unidade;
    após os dois laços para, criamos um vetor inter que
    irá conter exatamente os ind_inter elementos de
    interseção; e então mostramos a saída conforme
    solicitada.    
"""

# T1 = Ler o tamanho do primeiro vetor
T1 = int(input())

# V1 = Ler o primeiro vetor de inteiros
v = input().split()
V1 = T1*[0]
for i in range(T1):
    V1[i] = int(v[i])

# T2 = Ler o tamanho do segundo vetor
T2 = int(input())

# V2 = Ler o segundo vetor de inteiros
v = input().split()
V2 = T2*[0]
for i in range(T2):
    V2[i] = int(v[i])

# n recebe o menor tamanho entre T1 e T2
# para armazenar os valores de interseção
if T1 < T2:
    n = T1
else:
    n = T2

# pre_inter = vetor de n posições para os
# valores de interseção
pre_inter = n*[0]

# ind_inter será utilizado como índice de pre_inter
# e como quantidade de elementos de interseção
# ind_inter = 0
ind_inter = 0

# Os dois laços para servem para procurar
# cada elemento do primeiro vetor no segundo vetor
# para i de 0 a T1-1
for i in range(T1):
    # para j de 0 a T2-1
    for j in range(T2):
        # se V1[i] == V2[j]
        if V1[i] == V2[j]:
            # pre_inter[ind_inter] = V1[i]
            pre_inter[ind_inter] = V1[i]
            # ind_inter += 1
            ind_inter += 1
            # Se achou, já pode sair do segundo laço para
            break

# Se a quantidade de interseções ind_inter for
# menor que n então criamos um vetor inter com 
# exatamente ind_inter posições e colocamos
# os elementos de interseção em inter

# se ind_inter < n
if ind_inter < n:
    # n = ind_inter
    n = ind_inter
    # inter = n*[0]
    inter = n*[0]
    # para i de 0 a n-1
    for i in range(n):
        # inter[i] = pre_inter[i]
        inter[i] = pre_inter[i]
# senão
else:
    # inter = pre_inter
    inter = pre_inter

# se n == 0
if n == 0:
    # Mostrar "Não há interseção!"
    print("Não há interseção!")
# senão
else:
    # Mostrar "Elementos de interseção:"
    print("Elementos de interseção:")
    # elementos = ""
    elementos = ""
    # para i de 0 a n-2
    for i in range(n-1):
        # elementos += str(inter[i]) + " "
        elementos += str(inter[i]) + " "
    # elementos += str(inter[n-1])
    elementos += str(inter[n-1])
    # Mostrar elementos
    print(elementos)