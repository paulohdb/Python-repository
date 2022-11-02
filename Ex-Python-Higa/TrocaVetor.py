def troca(N: list):
    i = 0
    j = 19

    while i < j:
        temp = N[i]
        N[i] = N[j]
        N[j] = temp
        i += 1
        j -= 1

#===================================

def imprime(N: list):
    for i in range(len(N)):
        print(f"N[{i}] = {N[i]}")

#===================================

def main():
    N = []
    for i in range(20):
        num = int(input())
        N.append(num)

    troca(N)
    
    imprime(N)
    

#===================================

main()