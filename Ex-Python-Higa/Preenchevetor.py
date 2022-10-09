# Função para imprimir a lista de forma formatada
def imprime(N: list):

    # para cada i num alcance do tamanho da lista
    for i in range(len(N)):

        # print o valor e o index do valor
        print(f"N[{i}] = {N[i]}")

#============================================

# Função para preencher a lista com os valores multiplicados
def preencheVetor(lista: list):

    # Para cada i num alcance de 9 vezes
    # Começando em 0, pois o primeiro valor está em zero
    # na lista.
    for i in range(0, 9):
        # Cada vez, a lista fazerá um append, no 
        # item da lista i, multiplicado por 2
        lista.append(lista[i] * 2)

#============================================

def main():
    # Lendo o primeiro valor
    v = int(input())

    # Criando a lista N
    N = []

    # Adicionando o valor v, subsequente para os
    # outros resultados.
    N.append(v)

    # Chamar a função que irá preencher o resto da lista
    preencheVetor(N)

    #Chamar a função de imprimir formatado o resultado
    imprime(N)

#============================================

main()

        
