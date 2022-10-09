# função para calcular fibbonaci até o 60° número
# e retornar 
def fibo() -> list:

    # Criar uma lista com 61 zeros
    F = [0] * 61

    # Colocar no index 1, o valor de número 1
    F[1] = 1

    # Para i num alcance de 2 até 60
    for i in range(2, 61):

        # F[i] recebe F[i - 1] + F[i - 2]
        F[i] = F[i - 1] + F[i - 2]
    
    # Retorna a lista F
    return F

#========================================

def main():

    T = int(input())

    F = fibo()

    while T > 0:
        n = int(input())

        print(f"Fib({n}) = {F[n]}")

        T -= 1

#========================================

main()