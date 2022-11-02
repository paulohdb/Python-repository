def calculaVet(u, v: list) -> list:

    res = 0.0

    for i in range(len(u)):

        res = res + u[i] * v[i]

    return res

#=============================================

def main():

    u = list(map(float, input().split()))
    v = list(map(float, input().split()))

    valor = calculaVet(u, v)

    print(f"{valor:.4f}")

#=============================================

main()