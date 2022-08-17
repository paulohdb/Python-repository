#Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos 
#([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, 
#deverá ser impressa a mensagem “Fora de intervalo”.

#Ler um valor input
n_float = input()

#Transformar em um número flutuante(float)
n = float(n_float)
#Então, n receberá o valor de n_float, para agora ser a variável n 

#Estrutura de vericicação do valor n

#Se o valor n for maior igual a zero E n for menor igual a 25.00
if n >= 0 and n <= 25.00:
    #Imprimir na tela o intervalo pertencente ao primeiro If!
    print("Intervalo [0,25]")
#Atenção ao detalhe, a partir desse primeiro elif, o valor não poderá ser comparado como
#25.00, pois ele já está sendo comparado no primeiro intervalo.
#Aqui devemos acrescentar uma unidade, pois ela será o intervalo entre 25 e 50.
elif n >= 25.01 and n <= 50.00:
    #imprimir na tela o intervalo pertencente do elif (25,50)
    print("Intervalo (25,50]")
#Se n maior igual que 50.01 e n menor igual a 75.00, verificando se o número lido
#está entre 50 e 75.
elif n >= 50.01 and n <= 75.00:
    #imprimir na tela o intervalo pertencente do elif (50,75)
    print("Intervalo (50,75]")
#Se n maior igual que 75.01 e n menor igual a 100.00, verificando se o número lido
#está entre 75 e 100.
elif n >= 75.01 and n <= 100.00:
    #imprimir na tela o intervalo pertencente do elif (75,100)
    print("Intervalo (75,100]")
#Se não,imprimir "Fora de intervalo."
else:
    print("Fora de intervalo")

