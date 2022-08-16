frase = input().strip().upper()

palavras = frase.split()
join = "".join(palavras)

inverso = join[::-1]

"""
for i in range(len(join) -1, -1 ,-1):

    inverso += join[i]
"""


if join == inverso:

    print("Temos um palíndromo")

else:
    print("A frase não é um palíndromo")