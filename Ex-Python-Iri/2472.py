'''
    O Código iniciará com um input de valor inteiro para saber, quantos valores
    serão colocados na próxima linha. 

    Criar mais um input com split para e logo em seguida, listar as strings lidas.

    fazer a mesma coisa com a segunda leitura de vetores.

    Usaremos um for até o tamanho da lista1, v1 recebe vetor1 i vezes.
    Logo depois teremos outro for até o tamanho da lista, mas agora,
    verificando se v1 está em cada item de v2.

    Se caso não ter elementos, imprimir não há interseção. caso o contrário
    imprimir "elementos de interseção com os números abaixo.
'''

# ler um inteiro t1
t1 = int(input())

# ler um vetor1 com split
vet1 = input().split()

# listar os elementos do vetor1
lst1 = [vet1]

# ler um inteiro t2
t2 = int(input())

# ler um vetor1 com split
vet2 = input().split()

# listar os elementos do vetor2
lst2 = [vet2]


# para i até tamanho da lista1 - 1
for i in range(len(lst1)):

    # v1 recebe vetor1[i]
    v1 = vet1[i]
    
    # para j até tamanho da lista1 - 1
    for j in range(len(lst1)):

        # se v1 EM vetor2[j]
        if v1 in vet2[j]:

            # imprimir não há interseção
            print("Não há interseção!")
        
        # senão
        else:
            # imprimir elementeos de interseção com os números abaixo
            print("Elementos de interseção:")