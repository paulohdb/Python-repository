P1, Np1, valorp = input().split()
P2, Np2, valorp2 = input().split()

P1 = int(P1)
Np1 = int(Np1)
valorp = float(valorp)

P2 = int(P2)
Np2 = int(Np2)
valorp2 = float(valorp2)

Vap1 = Np1 * valorp
Vap2 = Np2 * valorp2

VaP = Vap1 + Vap2

print("VALOR A PAGAR: R$ {:.2f}" .format(VaP))