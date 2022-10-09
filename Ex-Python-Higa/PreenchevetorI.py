def preenche(T: int) -> list:
    N = [0] * 1000

    num = 0

    for i in range(len(N)):
        
        N[i] = num
        num += 1
        if num == T:
            num = 0
    
    return N

#=========================================

def imprime(N: list):
    for i in range(len(N)):
        print(f"N[{i}] = {N[i]}")

#=========================================

def main():
    T = int(input())

    N = preenche(T)

    imprime(N)

#=========================================

main()