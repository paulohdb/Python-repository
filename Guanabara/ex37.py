from lib2to3.pytree import convert


n = int(input("Digite o valor:"))

bas = int(input("Qual base de conversão?"))


if bas == 1:
    print("O número {} convertido para binário é {}" .format(n, bin(n)[2:]))

elif bas == 2:
    print("O número {} convertido para octal é {}" .format(n, oct(n)[2:] ))

elif bas == 2:
    print("O número {} convertido para hexadecimal é {}" .format(n, hex(n)[2:]))

else:
    print("Opção inválida")