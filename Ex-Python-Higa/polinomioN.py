def formula(lista: list, n: float):

    a = len(lista) - 1

    cont = 0

    for i in range(len(lista)):

        if a > 0:
            f1 = lista[i] * (n ** a)
            
            a -= 1
            cont += f1
        else:
            f2 = lista[-1]

            cont += f2

    print(f'{cont:.4f}')

#==========================================

def main():

    val = list(map(float, input().split()))

    val.reverse()

    k = int(input())

    while k > 0:

        n = float(input())

        formula(val, n)

        k -= 1

#============================================

main()