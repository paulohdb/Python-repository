v = int(input())

if v > 80:
    
    multa = (v - 80) * 7

    print("O valor da multa é de R${:.2f}" .format(multa))

else:
    print("Está andando perante a lei")