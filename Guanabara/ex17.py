import math

cat_str, cato_str = input("Digite o valor dos catetos: ").split()

cat = float(cat_str)
cato = float(cato_str)

hip = math.hypot(cat, cato)

print("O valor da hipotenusa é: {}" .format(hip))