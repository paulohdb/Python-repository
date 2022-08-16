n1 = int(input("Primeiro valor: "))

n2 = int(input("Segundo valor: "))

option = 0
while option != 5:
    print("""    [ 1 ] somar 
    [ 2 ] multiplicar
    [ 3 ] maior 
    [ 4 ] novos números
    [ 5 ] sair do programa""")

    option = int(input("Qual a sua opção?: "))

    if option == 1:
        soma = n1 + n2
        print("A soma entre {} e {} é igual à {}" .format(n1, n2, soma))
    elif option == 2:
        produto = n1 * n2
        print("O resultado de {} x {} é igual à {}" .format(n1, n2. produto))
    elif option == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("Entre {} e {} o maior valor é {}" .format(n1, n2, maior))
    elif option == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif option == 5:
        print("Finalizando...")

    else:
        print("Opção inválida, Tente uma opção válida")

print("Volte sempre!")