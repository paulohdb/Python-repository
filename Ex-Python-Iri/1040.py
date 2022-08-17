
N1, N2, N3, N4 = input().split()

n1 = float(N1)
n2 = float(N2)
n3 = float(N3)
n4 = float(N4)

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print("Media: {:.1f}" .format(media))


if media >= 7.0:
    print("Aluno aprovado.")

elif media < 5.0:
    print("Aluno reprovado.")

elif (media >= 5.0) and (media < 6.9):
    print("Aluno em exame.")
    
    nota2 = float(input())
    print("Nota do exame: {:.1f}" .format(nota2))
    media2 = (((nota2) + media)) / 2

    if media2 >= 5.0:
        print("Aluno aprovado.")
        print("Media final: {:.1f}" .format(media2))
    else:
        media2 <= 4.9
        print("Aluno reprovado.")


