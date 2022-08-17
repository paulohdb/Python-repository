'''
    Faça um algoritmo para ler um número indeterminado de dados,
    contendo cada um, a idade de um indivíduo. 
    O último dado, que não entrará nos cálculos, 
    contém o valor de idade negativa. 
    Calcular e imprimir a idade média deste grupo de indivíduos.
'''

#Atribuir um valor positivo para y para iniciar o laço while
y = 1
#Soma recebe 0
soma = 0
#n recebe 0
n = 0

#enquanto y for maior ou igual a 0
while y >= 0:

    #Ler um valor y inteiro
    y = int(input())

    #Se y for maior igual a zero
    if y >= 0:

        #então n recebe n + 1
        n = n + 1

        #então soma recebe soma + y
        soma = soma + y

    #Calcular a média recebendo soma sobre o valor n
    media = soma / n
    
#Imprimir o valor da média com duas casas decimais
print("{:.2f}" .format(media))  
        
