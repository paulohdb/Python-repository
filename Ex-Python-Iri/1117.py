'''
Faça um programa que leia as notas referentes às duas avaliações de um aluno.
Calcule e imprima a média semestral. 
Faça com que o algoritmo só aceite notas válidas 
(uma nota válida deve pertencer ao intervalo [0,10]). 
Cada nota deve ser validada separadamente.
Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
Quando duas notas válidas forem lidas, 
deve ser impressa a mensagem "media = " seguido do valor do cálculo. 
O valor deve ser apresentado com duas casas após o ponto decimal.

'''


#Para entrarmos no laço while, atribuimos o valor de 0 para i
i = 0 

#media recebe 0
media = 0

#enquanto i for menor que qualquer número maior que ele. Ex: 2
while i < 2:

    #Ler um valor float
    nota = float(input())

    #Se nota for maior ou igual a zero E nota for menor ou igual a 10
    if nota >= 0 and nota <= 10:

        #então i recebe i + 1
        i = i + 1

        #media recebe media + nota
        media = media + nota
    
     #Se nota for menor que 0 OU nota for maior que 10
    if nota < 0 or nota > 10:
        #então imprimir nota invalida
        print("nota invalida")

#Para calcular o media, media recebe a própria média divido por 2
media = media / 2

#Imprimir a média com duas casas decimais
print("media = {:.2f}" .format(media))