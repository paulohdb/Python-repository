'''
O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X for igual a 0). 
Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X , se for par. 
Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação: 4+6+8+10+12, 
enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a soma de 12+14+16+18+20.
'''

#Enquanto for verdadeiro
while True:
    #p recebe um valor inteiro do int
    p = int(input())

    #Se p == 0, parar o código
    if p == 0:
        #comando brake para ter o travamento do código.
        break
    #Se p for dividio inteiro por 2 e ser igual a 0. (verificação se é um número par)
    if p % 2 == 0:
        #start receberá o valor p.
        start = p
    #Se p não for um número par
    else:
        #start receberá o valor p + 1, para obter o próximo valor par do número impar
        start = p + 1
    
    #Nova variável soma receberá o valor start, sendo o primeiro número da soma
    soma = start

    #Para cada i de 1 a 4
    for i in range(4):

        #start receberá o valor de start mais 2
        start = start + 2

        #soma receberá o valor de soma mais start
        soma = soma + start

    #Imprimir a variável soma, pois essa variável contém o valor somado dos pares consecutivos
    print(soma)