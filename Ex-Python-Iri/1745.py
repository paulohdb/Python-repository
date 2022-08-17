#Apenas um input para obter o valor 

Ns = input()
N = int(Ns)
print("{}:".format(N))

#Milhar irá dividir o número por 1000 para descobrir quantos Milhares teremos!

milhar = N // 1000
N = N - (milhar * 1000)

#O que sobrou do milhar, vamos dividir por 100 para descobrir as centenas!!

centena = N // 100
N = N - (centena * 100)

#O que sobrou de centena, vamos dividir por 10 para descobrir as dezenas!!

dezena = N // 10
N = N - (milhar * 10)

#O que sobrou, teremos as unidades!

unidade = N

#Print para os valores obtidos pelo milhar, centena, dezena e unidade!

print("{} milhar(es)".format(milhar))
print("{} centena(s)".format(centena))
print("{} dezena(s)".format(dezena))
print("{} unidade(s)".format(unidade))