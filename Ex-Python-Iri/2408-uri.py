fs, gs = input().split()

#deixando eles como inteiro

f = int(fs)

g = int (gs)

#colocando os valores de 0

par = impar = divisivel_5 = intervalo = inteiros = 0

#calculando os valores dados por cada um deles para depois distribuir nos prints
for intervalo in range(f + 1, g):

    inteiros = intervalo
    if intervalo % 2 == 0:
        par += 1
    else:
        impar += 1
    if intervalo % 5 == 0:
        divisivel_5 += 1

#mostrando os resultados na tela com os prints

print("Intervalo ({}, {}):" .format(f, g))
print("Quantidade de inteiros: {}" .format(inteiros))
print("Quantidade de pares: {}" .format(par))
print("Quantidade de ímpares: {}" .format(impar))
print("Quantidade de divisíveis por 5: {}" .format(divisivel_5))