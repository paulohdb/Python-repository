num = ((int(input("1: "))), (int(input("2: "))), (int(input("3: "))), (int(input("4: "))))

print("Você digitou os valores {}" .format(num))

print("O valor 9 apareceu {} vezes" .format(num.count(9)))

if 3 in num:
    print("O valor 3 apareceu na {} posição" .format(num.index(3)+1))

else: 
    print("O valor 3 não foi digitado")

print("Od valores pares digitados foram ", end="")

for i in num:
    if i % 2 == 0:
        print(i, end="")
