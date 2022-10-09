
def imprime(lista: list):

    for i in range(len(lista)):

        if lista[i] <= 0:

            print(f"X[{i}] = 1")
            
        else:
            
            print(f"X[{i}] = {lista[i]}")
        
#=================================

def main():

    N = []

    for i in range(10):

        v = int(input())

        N.append(v)

    imprime(N)

#=================================

main()