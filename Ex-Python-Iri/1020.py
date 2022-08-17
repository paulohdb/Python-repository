#Apenas um input para obter o valor 

D = int(input())

#O "year" vai pegar o valor e dividir por 365, com parte inteira, para obter o valor de anos.

year = D // 365
D = D - year * 365

#O que sobrou do ano, vamos dividir por 30 para descobrir os meses!!

month = D // 30
D = D - month * 30

#O resto será os dias

days = D

print("{} ano(s)" .format(year))
print("{} mes(s)" .format(month))
print("{} dia(s)" .format(days))