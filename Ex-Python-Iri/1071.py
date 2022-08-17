'''
    Problema - 1071
    Leia 2 valores inteiros X e Y. A seguir, 
    calcule e mostre a soma dos números impares entre eles.
'''
#Ler dois números inteiros

#x = int(xs)
x = int(input())
#y = int(ys)
y = int(input())

#se x == y
if x == y:
    #então imprimir 0
    print(0)

#senão
else:

    #se x < y
    if x < y:
        #então start = x
        start = x
        #final = y
        final = y
    else:
        #start = y
        start = y
        #final = x
        final = x

    #se start for impar
    if start % 2 != 0:
        #então start = start + 2
        start = start + 2
    #senão:
    else:
        #start = start + 1
        start = start + 1

    #Se final for impar
    if final %2 != 0:
        #então final = final - 2
        final = final - 2
    #senão
    else:
        #final = final - 1
        final = final - 1

    # soma = 0
    soma = 0

    # for i de start até final, passo 2
    for i in range(start, final+1, 2):
        #somar = soma + i
        soma = soma + i

    #imprimir soma
    print(soma)