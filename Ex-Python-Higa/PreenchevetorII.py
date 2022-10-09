def imprime(lista: list):

    for i in range(len(lista)):

        if lista[i] <= 10.0:

            print(f"A[{i}] = {lista[i]:.1f}")

#===========================================

def main():

    A = []

    for i in range(0, 99):
        x = float(input())
        A.append(x)

    imprime(A)

#===========================================

main()