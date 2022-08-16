a1 = int(input())

razao = int(input())

dec = a1 + (10 - 1) * razao

for i in range(a1, dec + razao, razao):

    print(i)