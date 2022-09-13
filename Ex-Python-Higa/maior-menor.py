n = int(input())

num = int(input())

maior = menor = num 

for i in range(1, n):
    num = int(input())
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"Maior = {maior}")
print(f"Menor = {menor}")