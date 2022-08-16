a_str, b_str, c_str = input().split()

a = int(a_str)
b = int(b_str)
c = int(c_str)

menor = a 

if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c

maior = a

if b > a and b > c:
    maior = b

if c > b and c > a:
    maior = c

print ("O menor valor digitado é o {}" .format(menor))

print("O maior valor digitado é o {}" .format(maior))