'''
Ler 100 valores inteiros. Apresentar então o maior valor lido e a posição dentre os 100 valores lidos.
'''

#Ler um número nint inteiro
nint = int(input())

#firstpos recebe 1 
firstpos = 1

# Para i em um range de 2 a 100
for i in range(2, 101):
    #n irá ler um inteiro
    n = int(input())
    #Se n for maior que firstpos
    if n > nint:
        #nint receberá n
        nint = n
        #furstpos receberá i
        firstpos = i

#Imprimir o valor de nint
print(nint)
#Imprimir o valor de firstpos
print(firstpos)