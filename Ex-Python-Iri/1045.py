'''
    TIPOS DE TRIÂNGULOS
    Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, 
    de modo que o lado A representa o maior dos 3 lados. A seguir, 
    determine o tipo de triângulo que estes três lados formam,
    com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

    se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
    se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
    se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
    se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
    se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
    se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

'''
#Leia 3 valores de ponto flutuante
aS, bS, cS = input().split()

a = float(aS)
b = float(bS)
c = float(cS)


if c > b:
  aux = c
  c = b
  b = aux

if a < c:
  aux = c
  c = a
  a = aux

if a < b:
  aux = b
  b = a
  a = aux

#se A ≥ B+C
if a >= (b + c):
    #Imprimir NAO FORMA TRIANGULO
    print("NAO FORMA TRIANGULO")
    
#senao
else:
    #se A2 = B2 + C2
    if (a**2) == (b**2 + c**2):
        #Imprimir TRIANGULO RETANGULO
        print("TRIANGULO RETANGULO")
        
    #se A2 > B2 + C2
    if (a**2) > (b**2 + c**2):
        #Imprimir TRIANGULO OBTUSANGULO
        print("TRIANGULO OBTUSANGULO")
        
    #se A2 < B2 + C2
    if (a**2) < (b**2 + c**2):
        #Imprimir TRIANGULO ACUTANGULO
        print("TRIANGULO ACUTANGULO")
        
    #se os três lados forem iguais
    if (a == b == c):
        #Imprimir TRIANGULO EQUILATERO
        print("TRIANGULO EQUILATERO")
        
    #se apenas dois dos lados forem iguais
    if a == b != c or b == c != a  or a == c != b: 
        #Imprimir TRIANGULO ISOSCELES
        print("TRIANGULO ISOSCELES")
