'''
    Leia 5 valores Inteiros. 
    A seguir mostre quantos valores digitados foram pares,
    quantos valores digitados foram ímpares,
    quantos valores digitados foram positivos e
    quantos valores digitados foram negativos.
'''

#Ler 5 valores inteiros quaisquer

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

#par = 0
par = 0
#impar = 0
impar = 0
#positivo = 0
positivo = 0
#negativo = 0
negativo = 0

#Se a %2 == 0:
if a %2 == 0:
    #então par = par + 1
    par = par + 1
#Se b %2 == 0:
if b %2 == 0:
    #então par = par + 1
    par = par + 1
#Se c %2 == 0:
if c %2 == 0:
    #então par = par + 1
    par = par + 1
#Se d %2 == 0:
if d %2 == 0:
    #então par = par + 1
    par = par + 1
#Se e %2 == 0:
if e %2 == 0:
    #então par = par + 1
    par = par + 1

#Imprimir quantos valores são positivos
print("{} valor(es) par(es)" .format(par))

#Se a %2 != 0:
if a %2 != 0:
    #então impar = impar + 1
    impar = impar + 1

#Se b %2 != 0:
if b %2 != 0:
    #então impar = impar + 1
    impar = impar + 1

#Se c %2 != 0:
if c %2 != 0:
    #então impar = impar + 1
    impar = impar + 1

#Se d %2 != 0:
if d %2 != 0:
    #então impar = impar + 1
    impar = impar + 1

#Se e %2 != 0:
if e %2 != 0:
    #então impar = impar + 1
    impar = impar + 1

#imprimir quantos valores são pares
print("{} valor(es) impar(es)" .format(impar))

#Se a > 0:
if a > 0:
#então positivo = positivo + 1:
    positivo = positivo + 1

#Se b > 0:
if b > 0:
#então positivo = positivo + 1:
    positivo = positivo + 1

#Se c > 0:
if c > 0:
#então positivo = positivo + 1:
    positivo = positivo + 1

#Se d > 0:
if d > 0:
#então positivo = positivo + 1:
    positivo = positivo + 1

#Se e > 0:
if e > 0:
#então positivo = positivo + 1:
    positivo = positivo + 1

#imprimir quantos valores são positivos
print("{} valor(es) positivo(s)" .format(positivo))

#Se a < 0:
if a < 0:
#então negativo = negativo + 1:
    negativo = negativo + 1

#Se b < 0:
if b < 0:
#então negativo = negativo + 1:
    negativo = negativo + 1

#Se c < 0:
if c < 0:
#então negativo = negativo + 1:
    negativo = negativo + 1

#Se d < 0:
if d < 0:
#então negativo = negativo + 1:
    negativo = negativo + 1

#Se e < 0:
if e < 0:
#então negativo = negativo + 1:
    negativo = negativo + 1

#Imprimir quantos valores são negativos
print("{} valor(es) negativo(s)" .format(negativo))