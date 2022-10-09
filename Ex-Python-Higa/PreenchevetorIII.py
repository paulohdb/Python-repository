def imprime(N: list):

    for i in range(len(N)):
        print(f"N[{i}] = {N[i]:.4f}")

#===============================================

def vet(lista: list):

    for i in range(0, 99):
        lista.append(lista[i] / 2.0)

#===============================================

def main():

    X = float(input())

    N = [X]

    vet(N)

    imprime(N)

#===============================================

main()