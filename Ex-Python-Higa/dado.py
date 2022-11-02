def verifica(lista: list, n: int) -> list:

    timesD = [0] * 13

    for i in range(len(lista)):

        ind = 1

        for j in range(13):

            if lista[i] == ind:

                timesD[j] += 1

            ind += 1
    
    return timesD

#===================================================    

def calculaDado(lista: list, n: int) -> list:

    vef = []

    for i in range(len(lista)):

        if lista[i] == 0:

            vef.append(0)

        else:

            num = (lista[i] / n) * 100

            vef.append(num)

    return vef

#===================================================

def imprime(lista: list):

    print(f"Face 1: {lista[0]:.2f}%")

    for i in range(1, len(lista)):
        print(f"Face {i+1}: {lista[i]:.2f}%")

#===================================================

def main():

    n = int(input())

    dado = list(map(int, input().split()))

    dadover = verifica(dado, n)

    dadoest = calculaDado(dadover, n)

    imprime(dadoest)

#===================================================

main()