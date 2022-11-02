def verifica(lista, lis: list) -> list:

    cont = []

    for i in range(len(lista)):

        ind = 0

        for j in range(len(lis)):

            if (i + j) < len(lista):

                if lis[j] == lista[i + j]:

                    ind += 1
                
                if ind == len(lis):

                    cont.append(i)

    return cont

def imprime(lista: list):

 
    for i in range(len(lista)):
        print(f'{lista[i]}')


def main():

    frase = list(input())
    word = list(input())

    times = verifica(frase, word)

    if times == []:
        
        print("NOT FOUND!")

    else:
        imprime(times)
        
main()