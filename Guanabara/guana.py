# Listas

lanche = ["hamburguer", "suco", "pizza", "picole"]

lanche.append("cookie")

lanche.insert(0, "hotdog")

"""
    Cadernim de aprendizagem

    Ordem de precedência

    1 - ()
    2 - **
    3 - * / // %
    4 - + -


"""








# del lanche[3]

# print(lanche)

# valores = [5, 8, 2, 4, 19, 4, 43]

# valores.sort()


# valores.sort(reverse=True)

# print(len(valores))



# num = [2, 5, 7, 8, 1, 12]

# num[2] = 3

# num.append(6)

#print(num)
#print(f"Essa lista tem {len(num)} elementos")

"""
valores = []

for i in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

for c, i in enumerate(valores):

    print(f"Na posição {c} encontrei o valor {i}!")

print("Cheguei ao final da lista.")

"""

# Desafio 079 #
'''
lst = []

while True:

    valor = int(input("Digite um número: "))

    if valor not in lst:
        lst.append(valor)
        print("Valor adicionado com sucesso")

    else:
        print("Valor duplicado! Não vamos adicionar")

    while True:

        verifica = str(input("Quer continuar? [S/N] ")).upper()

        if verifica in "SN":
            break
        else:
            print("Resposta invalida.", end="")
    
    if verifica in "N":
        break
    
lst.sort()
print("Você digitou os valores: {}" .format(lst))

'''

# Desafio 080 #

"""
lst = []

for i in range(0, 5):

    n = int(input("Digite um valor: "))

    if i == 0 or n > lst[len(lst)-1]:
        lst.append(n)

    else:

        pos = 0

        while pos < len(lst):

            if n <= lst[pos]:
                lst.insert(pos, n)
                break
            
            pos += 1

print("Os valores digitados em ordem foram {}" .format(lst))

"""

"""
lst = []

while True:

    lst.append(int(input("Digitie um valor: ")))

    rep = str(input("Quer continuar? S/N ").upper())

    if rep in "N":
        break

print("Foram digitados {} números" .format(len(lst)))

lst.sort(reverse=True)

print("Lista de valores descrescente: {}" .format(lst))

if 5 in lst:
    print("O valor 5 faz parte da lista!")

else:
    print("O valor 5 não foi encontrado na lista")

"""

galera = []

dado = []

totma = totme = 0

for i in range(0, 3):

    dado.append(input("Nome: "))
    dado.append(int(input("Idade: ")))

    galera.append(dado[:])

    dado.clear()

for i in galera:

    if i[1] >= 21:

        print("{} é maior de idade." .format(i[0]))
        totma += 1

    else:
        print("{} é menor é idade." .format(i[0]))
        totme += 1

print("Temos {} maiores e {} menores de idade" .format(totma, totme))
