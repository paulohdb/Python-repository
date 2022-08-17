#O principal objetivo do código é lermos dois valores
#splitados, a partir deles iremos calcular o valor de compra
#de produtos.

#Primeiro passo é termos um input para ler os dois valores que
#será proporcionado na entrada. (Split e dois valores inteiros)
cod_item_int, cod_qtd_int = input().split()

#Convertemos str para int, fazendo com que o item e o qtd recebam as str do input
item = int(cod_item_int)
qtd = int(cod_qtd_int)


#Se item for igual a um, ele terá uma nova variavel "total"
if item == 1:
    #total receberá o valor int de qtd e multiplicará por 4.00,
    #valor esse disponível na tabela do exercício.
    total = qtd * 4.00
    #Imprimir o total, formatado com duas casas depois do ponto, usando o .format!
    print("Total: R$ {:.2f}" .format(total))

#Se item for igual a dois, ele terá uma nova variavel "total"
if item == 2:
    #total receberá o valor int de qtd e multiplicará por 4.50,
    #valor esse disponível na tabela do exercício.
    total = qtd * 4.50
    #Imprimir o total, formatado com duas casas depois do ponto, usando o .format!
    print("Total: R$ {:.2f}" .format(total))

#Se item for igual a três, ele terá uma nova variavel "total"
if item == 3:
    #total receberá o valor int de qtd e multiplicará por 5.00,
    #valor esse disponível na tabela do exercício.
    total = qtd * 5.00
    #Imprimir o total, formatado com duas casas depois do ponto, usando o .format!
    print("Total: R$ {:.2f}" .format(total))

#Se item for igual a quatro, ele terá uma nova variavel "total"
if item == 4:
    #total receberá o valor int de qtd e multiplicará por 2.00,
    #valor esse disponível na tabela do exercício.
    total = qtd * 2.00
    #Imprimir o total, formatado com duas casas depois do ponto, usando o .format!
    print("Total: R$ {:.2f}" .format(total))

#Se item for igual a quatro, ele terá uma nova variavel "total"
if item == 5:
    #total receberá o valor int de qtd e multiplicará por 1.50,
    #valor esse disponível na tabela do exercício.
    total = qtd * 1.50
    #Imprimir o total, formatado com duas casas depois do ponto, usando o .format!
    print("Total: R$ {:.2f}" .format(total))

