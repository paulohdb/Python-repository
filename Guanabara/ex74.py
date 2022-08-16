from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print("Os valores sorteados foram: ", end="")

for i in numeros:
    print("{} ", end="")

print("O maior valor sorteado foi {}" .format(max(numeros)))

print("O menor valor sorteado foi {}" .format(min(numeros)))