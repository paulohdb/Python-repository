import random

n1 = input("O nome do(a) aluno(a) é: ")
n2 = input("O nome do(a) aluno(a) é: ")
n3 = input("O nome do(a) aluno(a) é: ")
n4 = input("O nome do(a) aluno(a) é: ")

lst = [n1, n2, n3, n4]

sorte = random.choice(lst)

print("O aluno sorteado é o(a): {}" .format(sorte))
