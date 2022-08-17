'''
    PROBLEMA DE NÚMERO 1101 - SEQUENCIA DE NÚMEROS E SOMA

    O código usará while para ter uma leitura infinita até que um acondição
    (Algum dos valores lidos, sejem zero), para parar o código.

    Usaremos o while True, em seguida leremos dois valores m e n,
    para depois compararmos, se m maior que 0 e n maior que 0, prosseguir.

    Logo depois, teremos um for para pegarmos o valor do intervalo de m e n,
    e logo depois a soma deles.

    Imprimir os valores obtivdos pelo for do intervalo e a soma com "Sum="

    O senão, será usado caso os números m e n forem menor ou igual a zero.
    Aqui determinará o break, assim parando o código.
'''

# enquanto verdadeiro
while True:

    # Ler dois valores m e n
    m_str, n_str = input().split()

    # Converte-los em int
    m = int(m_str)

    n = int(n_str)

    # Se m maior que zero e n maior que zero
    if m > 0 and n > 0:


        for i in range(m, n-1):
            x = m + 1

    # Senão, parar o código.
    else:
        if m <= 0 and n <= 0:
            break