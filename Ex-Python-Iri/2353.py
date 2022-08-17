#Ler cinco códigos de curso de 5 Estudantes da UFMS, separados por espaços

v1s, v2s, v3s, v4s, v5s = input().split()

V1 = int(v1s)
V2 = int(v2s)
V3 = int(v3s)
V4 = int(v4s)
V5 = int(v5s)

#aqui funcionará da mesma forma que usamos para validar a atividade de identificar o chá!

inma = 0
facom = 0
outros = 0

#porém, estaremos usando o or, para comparar mais resultados para acrescentar na "pontuação" de quantos alunos tem em cada faculdade

if V1 == 1902 or V1 == 1904 or V1 == 1905 or V1 == 1906 or V1 == 1907:
    facom = facom + 1

if V2 == 1902 or V2 == 1904 or V2 == 1905 or V2 == 1906 or V2 == 1907:
    facom = facom + 1

if V3 == 1902 or V3 == 1904 or V3 == 1905 or V3 == 1906 or V3 == 1907:
    facom = facom + 1

if V4 == 1902 or V4 == 1904 or V4 == 1905 or V4 == 1906 or V4 == 1907:
    facom = facom + 1

if V5 == 1902 or V5 == 1904 or V5 == 1905 or V5 == 1906 or V5 == 1907:
    facom = facom + 1


if V1 == 2201 or V1 == 2202 or V1 == 2203 or V1 == 2291:
    inma = inma + 1

if V2 == 2201 or V2 == 2202 or V2 == 2203 or V2 == 2291:
    inma = inma + 1

if V3 == 2201 or V3 == 2202 or V3 == 2203 or V3 == 2291:
    inma = inma + 1

if V4 == 2201 or V4 == 2202 or V4 == 2203 or V4 == 2291:
    inma = inma + 1

if V5 == 2201 or V5 == 2202 or V5 == 2203 or V5 == 2291:
    inma = inma + 1

if V1 != 1902 and V1 != 1904 and V1 != 1905 and V1 != 1906 and V1 != 1907 and V1 != 2201 and V1 != 2202 and V1 != 2203 and V1 != 2291:
    outros = outros + 1

if V2 != 1902 and V2 != 1904 and V2 != 1905 and V2 != 1906 and V2 != 1907 and V2 != 2201 and V2 != 2202 and V2 != 2203 and V2 != 2291:
    outros = outros + 1

if V3 != 1902 and V3 != 1904 and V3 != 1905 and V3 != 1906 and V3 != 1907 and V3 != 2201 and V3 != 2202 and V3 != 2203 and V3 != 2291:
    outros = outros + 1

if V4 != 1902 and V4 != 1904 and V4 != 1905 and V4 != 1906 and V4 != 1907 and V4 != 2201 and V4 != 2202 and V4 != 2203 and V4 != 2291:
    outros = outros + 1

if V5 != 1902 and V5 != 1904 and V5 != 1905 and V5 != 1906 and V5 != 1907 and V5 != 2201 and V5 != 2202 and V5 != 2203 and V5 != 2291:
    outros = outros + 1

#Print para imprimir os valores!

print("Facom: {}" .format(facom))
print("Inma: {}" .format(inma))
print("Outras unidades: {}" .format(outros))