n = int(input())

cont = 0

for i in range(2, n):

    if n % i == 0:
        cont += 1
        break
    
if cont == 0:
    print("Primo")
else:
    print("Composto")