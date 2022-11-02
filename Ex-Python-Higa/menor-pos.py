def menorNum(X: list):
    
    menor = X[0]
    i_menor = 0

    for i in range(1, len(X)):
        
        if X[i] < menor:
            menor = X[i]
            i_menor = i
    
    return menor, i_menor

#===========================================

def main():
    n = int(input())
    X = list(map(int, input().split()))

    menor, pos = menorNum(X)

    print(f"Menor valor: {menor}")
    print(f'Posicao: {pos}')

#===========================================,

main()