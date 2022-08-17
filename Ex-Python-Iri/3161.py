'''
    O inicio do código, conterá um input, que lerá dois valores INTEIROS
    na mesma linha. assim definindo em m e n inteiros do primeiro e o segundo valor.

    Criar dois vetores, um para as frutas multiplicando a lista em m, e o outro
    vetor das linhas codificadas multiplicando a lista em n.

    Logo, a criação de dois for, será para colocar em letras minusculas, os 
    dois vetores criados acima.

    Em seguida, o próximo for, será de um for até m vezes. 
    Dentro dele conterá:

    uma variável fruta recebendo vetorf[i], para percorrer em todas as letras.
    uma variável aturf recebendo fruta invertido,
    uma variavel de valor booleano find,

    A utilização do segundo for, será para verificar se fruta ou aturf,
    está no vetorc, da lista de linhas codificadas. Se caso tiver, find recebe
    True, e saimos daquele laço.

    Ao voltar para o primeiro for, se find for verdadeiro, mostrar que o
    Sheldon gosta daquela fruta

    Caso o contrário (senão), mostrar que o Sheldon detesta aquela fruta.

'''

# line recebe um input split
line = input().split()

# Transformar os valores lidos em inteiros m e n
m = int(line[0])
n = int(line[1])

# vetor de frutas recebe m*[""]
vetorf = m*[""]

# vetor de linhas codificadas recebe n*[""]
vetorc = n*[""]

# Aqui terá dois for para converter tudo em letras minusculas.

# para i até m:
for i in range(m):

    # vetor i recebe input com a função lower
    vetorf[i] = input().lower()

# para i até n:
for i in range(n):

    # vetor i recebe input com a função lower
    vetorc[i] = input().lower()


# para i até m:
for i in range(m):

    # fruta recebe vetorf[i]
    fruta = vetorf[i]

    # aturf recebe fruta ao contrário.
    aturf = fruta[::-1]

    # find é atribuido o valor booleano False
    find = False

    # para j até n
    for j in range(n):

        # se a fruta estiver no vetorc OU fruta invertida estiver em vetorc
        if fruta in vetorc[j] or aturf in vetorc[j]:

            # find recebe o valor booleano True
            find = True

            # Sair do laço for
            break
    
    # Se find for verdadeiro
    if find:
        
        # Imprimir que sheldon come a fruta
        print("Sheldon come a fruta", fruta)

    # Senão
    else:

        # Imprimir que sheldon detesta a fruta
        print("Sheldon detesta a fruta", fruta)