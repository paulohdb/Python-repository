# -*- coding: utf-8 -*-

# v = 100*[0.0]
v = 100*[0.0]

# para i de 0 até 99
for i in range(100):
    # v[i] = real(Ler entrada)
    v[i] = float(input())
    
# para i de 0 até 99
for i in range(100):
    # se v[i] <= 10
    if v[i] <= 10:
        # Mostrar "A["i"] = "v[i]
        print("A[{0:d}] = {1:.1f}".format(i, v[i]))