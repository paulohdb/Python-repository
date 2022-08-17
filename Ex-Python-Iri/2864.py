'''
    PROBLEMA DE NÚMERO 2864 - QUAL É A ALTURA?

    O começo do código terá um input que lerá um valor inteiro,
    esse o valor que dirá quantas vezes iremos rodar o caso de teste.

    O caso de teste usará um for i in range (variável do input), 
    dentro desse for, conterá as 3 variáveis a, b e c, que serão lidas em str
    e será splitadas. Logo em seguida, converter esses valores para inteiro.

    A variável delta, calculará o delta, variável que será utilizado no yv, 
    para calcular exatamente a altura máxima que a fruta alcançou no arremesso.

    sendo:

    delta = (b ** 2) - 4*(a*c) 
    yv = (-delta) / (4 * a)

    Ao final, teremos um print com duas casas decimais após o ponto.
'''

# Ler um valor inteiro t
t = int(input())


# para i até t
for i in range(t):

    # variaveis a, b e c sendo lidos em um input, para assim splitar
    a_str, b_str, c_str = input().split()

    # Converter os valores em inteiros
    a = int(a_str)

    b = int(b_str)

    c = int(c_str)

    # Realizar o calculo de delta
    delta = (b ** 2) - 4*(a*c)

    # Realizar o calculo de yv, valor da altura.
    yv = (-delta) / (4 * a)

    # Imprimir o valor de yv com duas casas decimais após o ponto.
    print("{:.2f}" .format(yv))
