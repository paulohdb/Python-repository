km = float(input("Quantos Km foi rodado?: "))

days = int(input("Quantos dias ficou alugado: "))

kmr = km * 0.15

daysa = days * 60.00

soma = kmr + daysa

print("O preço de tudo ficou: R${:.2f}" .format(soma))