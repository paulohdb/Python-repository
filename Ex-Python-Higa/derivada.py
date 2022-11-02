def formula(lista: list) -> list:

    a = len(lista) - 1

    li = []

    for i in range(a):

        if a > 1:

            f1 = lista[i] * a

            li.append(f1)

            a -= 1
        
        else:
            li.append(lista[-2])

    return li

def imprime(lista: list):

    lista.reverse()

    for i in range(len(lista)):

        print(f"{lista[i]:.4f}")

def main():

    val = list(map(float, input().split()))

    val.reverse()

    valor = formula(val)

    imprime(valor)

main()