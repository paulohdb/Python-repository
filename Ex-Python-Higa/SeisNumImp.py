def main():

    N = int(input())

    if N % 2 == 0:
        imp = N + 1
    
    else:
        imp = N
    
    for i in range(6):

        print(imp)

        imp += 2

main()