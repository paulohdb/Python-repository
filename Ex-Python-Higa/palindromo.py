def verifica(me: str) -> str:

    lista = list(me)

    i = 0
    j = len(lista) - 1

    while i < j:

        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp
        
        i += 1
        j -= 1

    jacuzi = "".join(lista)

    return jacuzi

def main():

    n = (input().split())

    m = "".join(n)

    p = verifica(m)

    if m == p:
        print("SIM")
    else:
        print("NAO")

main()