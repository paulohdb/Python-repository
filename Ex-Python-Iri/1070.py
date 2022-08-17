'''
    Leia um valor inteiro X. Em seguida apresente os 
    6 valores ímpares consecutivos a partir de X,
    um valor por linha, inclusive o X ser for o caso.
'''
#Ler x recebendo um input inteiro
x = int(input())

#Se x for par
if x % 2 == 0:
    #Então impar = x + 1
    impar = x + 1
#Senão
else:
    #impar = x
    impar = x

#para i de 1 a 6
for i in range(6):
    #Imprimir impar
    print(impar)
    #impar = impar + 2
    impar = impar + 2