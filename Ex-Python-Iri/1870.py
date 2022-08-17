
m = []

Lstr, Cstr, Pstr = input().split()

linha = int(Lstr)

coluna = int(Cstr)

position = int(Pstr)

for i in range(linha):
    
    lst_linha = []

    for i in range(linha):

        lst_linha.append(input())
    
    m.append(lst_linha)
    
print(m)
