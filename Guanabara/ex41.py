from datetime import date

atual = date.today().year

born = int(input("Ano de nascimento: "))

idade = atual - born

print("O atleta tem {} anos" .format(idade))

if idade < 9:
    print("Atleta MIRIM")

elif idade >= 9 and idade < 14:
    print("Atleta Infantil")

elif idade >= 14 and idade < 19:
    print("Atleta Júnior")

elif idade >= 19 and idade < 25:
    print("Atleta Senior")

else: 
    print("Atleta Master")