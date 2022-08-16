r1 = float(input())
r2 = float(input())
r3 = float(input())

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos PODEM FORMAR um triangulo", end="")

    if r1 == r2 == r3:
        print("Equilátero")

    elif r1 != r2 != r3 != r1:
        print("Escaleno!")

    else:
        print("Isóceles")
    
else:
    print("Os segmentos NÃO PODEM FORMAR um triangulo")