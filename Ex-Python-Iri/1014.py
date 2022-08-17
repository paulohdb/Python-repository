'''
    beecrowd | 1014 Consumo
Calcule o consumo médio de um automóvel sendo
fornecidos a distância total percorrida
(em Km) e o total de combustível gasto (em litros).
'''

#Ler valor X inteiro
X = int(input())

#Ler valor Y com um digito após o ponto decimal
Y = float(input())

media = X / Y

print("{:.3f} km/l" .format(media))