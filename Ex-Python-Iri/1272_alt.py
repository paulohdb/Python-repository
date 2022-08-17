# -*- coding: utf-8 -*-

# n = Ler a quantidade de casos de teste,
# ou de strings
n = int(input())

# para i de 1 até n
for i in range(n):
# for i in range(0, n):
# for i in range(1, n+1):
    # st = Ler uma string
    st = input()
    # lst = Dividir a string st utilizando o
    # espaço como separador entre componentes
    # e gerar uma lista
    lst = st.split()
    
    # tam = tamanho(lst)
    tam = len(lst)
    
    # msg_oculta = ""
    msg_oculta = ""
    
    # para j de 0 até tam-1
    for j in range(tam):
    # for j in range(0, tam):        
        # msg_oculta = msg_oculta + lst[j][0]
        msg_oculta = msg_oculta + lst[j][0]
    
    # Mostrar msg_oculta
    print(msg_oculta)
    
        