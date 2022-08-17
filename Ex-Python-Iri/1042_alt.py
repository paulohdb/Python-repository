'''
  Leia 3 valores inteiros e ordene-os em ordem crescente. 
  No final, mostre os valores em ordem crescente, 
  uma linha em branco e em seguida, 
  os valores na sequência como foram lidos.
'''


# Ler 3 números inteiros
xs, ys, zs = input().split()
x = int(xs)
y = int(ys)
z = int(zs)

#Ordenar os 3 números em ordem crescente 
if x > y:
  aux = x
  x = y
  y = aux
# Neste ponto sabemos que x <= y
if z < x:
  aux = x
  x = z
  z = aux
# Neste ponto sabemos que x <= y e x <= z
if z < y:
  aux = y
  y = z
  z = aux
  # Neste ponto sabemos que x <= y e x <= z, e y <= z
# Mostrar os 3 números em ordem crescente
print(x)
print(y)
print(z)

# Pular linha
print()

# Mostrar os 3 valores na ordem original
print(xs)
print(ys)
print(zs)
