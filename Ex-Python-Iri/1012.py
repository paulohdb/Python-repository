A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)
pi = 3.14159

Atri = A * C / 2
Acir = pi * C**2
Atra = (A + B) * C / 2
Aqua = B**2
Aret = A * B

print("TRIANGULO: {:.3f}" .format(Atri))
print("CIRCULO: {:.3f}" .format(Acir))
print("TRAPEZIO: {:.3f}" .format(Atra))
print("QUADRADO: {:.3f}" .format(Aqua))
print("RETANGULO: {:.3f}" .format(Aret))