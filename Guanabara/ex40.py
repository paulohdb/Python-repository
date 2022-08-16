n1 = float(input("Primeira nota: "))

n2 = float(input("Segunda nota: "))

media = (n1 + n2) / 2

if media >= 7.0:
    
    print("O aluno foi aprovado")

elif media < 5.0:
    print("O aluno foi reprovado")

elif media >= 5.0 and media <= 6.9:
    print("O aluno está de recuperação")