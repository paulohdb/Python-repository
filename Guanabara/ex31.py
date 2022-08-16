n = int(input())

if n >= 200:

    viagem1 = n * 0.45

    print("Sua viagem deu R${:.2f}" .format(viagem1))

else:

    viagem2 = n * 0.50

    print("Sua viagem deu R${:.2f}" .format(viagem2))