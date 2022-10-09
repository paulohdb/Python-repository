def imprimePar(lista: list):

    for i in range(len(lista)):

        print(f"par[{i}] = {lista[i]}")

    lista.clear()

#==========================================

def imprimeImp(lista: list):
    for i in range(len(lista)):

        print(f"impar[{i}] = {lista[i]}")

    lista.clear()

#==========================================

def main():

    par = []
    imp = []

    for i in range(15):

        num = int(input())

        if num % 2 == 0:

            par.append(num)
            
            if len(par) == 5:
                imprimePar(par)
        
        else:

            imp.append(num)

            if len(imp) == 5:
                imprimeImp(imp)
    
    for i in range(len(imp)):
        print(f"impar[{i}] = {imp[i]}")

    for i in range(len(par)):
        print(f"par[{i}] = {par[i]}")

#==========================================

main()