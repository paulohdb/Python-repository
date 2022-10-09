def somaUm(x):
    x = x + 1
    return x
#========================

def fat(y):
    fator = 1

    for i in range(1, y+1):
        fator = i * fator

    return fator
#========================

def main():
    x = 10
    i = 3
    soma = somaUm(x)
    fator = fat(i)
    res = fator + soma
    print(res)

main()
