
# Exercício 1272
# Nesse exercicio usaremos um input inteiro para verificar
# quantos códigos ocultos iremos ler.
# Depois, usaremos um For para ler o valor str, uma variavel de tamanho
# e a mensagem oculta para concatenar!
# Usaremos outro for para verificar cada inicial de cada palavra lida do str.
# Por fim teremos um print da mensagem oculta.


# Ler um valor inteiro n
n = int(input())

# Para i in range n
for i in range(n):

    # Strin recebe um input
    strin = input()

    # lst recebe strin para splitar
    lst = strin.split()

    # Nova variavel tamanho com função len, para ter o tamanho de lst
    tamanho = len(lst)

    # ocult recebe um valor vazio para concatenarmos
    ocult = ""

    # Para j in range tamanho
    for j in range (tamanho):

        # word recebe lst[j]
        word = lst[j]

        # ocult recebe ocult mais word, porém com o valor [0]
        # para termos a letra inicial de cada palavra.
        ocult = ocult + word[0]

    # Por fim, imprimir a mensagem oculta.
    print(ocult)