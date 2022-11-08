def fazMatriz():

    n = 1

    while n > 0:

        n = int(input())

        A = [[0] * n for i in range(n)]

        for i in range(n):

            for j in range(n):

                A[i][j] = 1
        
        for i in range(n):

            for j in range(n):

                print(f"  {A[i]}", end=' ')

def main():

    fazMatriz()

main()