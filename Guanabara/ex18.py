import math

a = float(input("Digite um ângulo: "))

sen = math.sin(a)

cos = math.cos(a)

tan = math.tan(a)

print("O seno de {}° é {:.2f}°" .format(a, math.degrees(sen)))
print("O cosseno de {}° é {:.2f}°" .format(a, math.degrees(cos)))
print("O tangente de {}° é {:.2f}°" .format(a, math.degrees(tan)))