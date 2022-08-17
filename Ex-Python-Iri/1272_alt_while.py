# -*- coding: utf-8 -*-

# n = Ler a quantidade de casos de teste,
# ou de strings
n = int(input())

i = 1

while (i <= n):
    # lst = Ler a string e dividir a string st utilizando o
    # espaço como separador entre componentes
    # e gerar uma lista
    lst = input().split()
    
    # tam = tamanho(lst)
    tam = len(lst)
    
    # msg_oculta = ""
    msg_oculta = ""
    
    j = 0
    while j < tam:
    # for j in range(0, tam):        
        # msg_oculta = msg_oculta + lst[j][0]
        msg_oculta = msg_oculta + lst[j][0]
        j = j + 1
    
    i = i + 1
    
    # Mostrar msg_oculta
    print(msg_oculta)
    
        