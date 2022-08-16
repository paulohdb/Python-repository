lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata Frita")

for i in lanche:
    print("Eu vou comer {}" .format(i))

for i in range(0, len(lanche)):
    print("Eu vou comer {} na posição {}" .format(lanche[i], i))

for pos, i in enumerate(lanche):
    print("Eu vou comer {} na posição {}" .format(i, pos))

print("Comi pra caramba!")