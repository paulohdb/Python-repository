'''
    Ler um valor N. Calcular e escrever seu respectivo fatorial.
    Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.
'''

#ler um valor inteiro.

n = int(input())

#calcular o fatorial de N.

#fator recebe 1
fator = 1

#para cada i num alcance de 1 até o número que desejamos MAIS um
for i in range (1, n+1):
    #fator irá receber i vezes o fator
    fator = i * fator

#imprimir fator
print(fator)
    