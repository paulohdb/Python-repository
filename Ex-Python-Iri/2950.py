'''
    PROBLEMA NÚMERO 2950 - AS DUAS TORRES

    O código no momento inicial, terá um input, com leitura de 
    três valore splitados, todos inteiros.

    O cálculo do ICM irá dividir a distancia entre as duas Palantirs,
    pela soma do diametro dos mesmos.

    Por fim, imprimir o resultado em valor real, com duas casa deciamsi.
'''

# Ler 3 valores e separá-los
dis_pt, dia_ptesa, dia_ptsaru = input().split()


# n recebe distancia do palantir para inteiro
n = int(dis_pt)

# x recebe o diametro de Palantir Sauron para inteiro
x = int(dia_ptesa)

# y recebe o diametro de Palantir de Saruman
y = int(dia_ptsaru)

# Calcular a soma dos diametros dos palantirs
soma = x + y

# Calcular a divisão da soma dos diametros "soma"
icm = n / soma

# Imprimir o valor de IMC com duas casas decimais.
print("{:.2f}" .format(icm))