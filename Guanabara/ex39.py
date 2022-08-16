from datetime import date

atual = date.today().year

born = int(input("Ano de nascimento: "))

idade = atual - born

print("Quem nasceu em {} tem {}".format(born, idade))

if idade == 18:

    print("Se aliste IMEDIATAMENTE")

elif idade < 18:
    saldo = 18 - idade

    print("Você ainda não tem 18 anos. Faltam {} anos para o alistamento" .format(saldo))

    ano = atual + saldo

    print("Seu alistamento será em {}" .format(ano))

elif idade > 18:
    saldo = idade - 18
    
    print("Você já deveria ter se alistado há {} anos" .format(saldo))

    ano = atual - saldo

    print("Seu alistamento foi em {}" .format(ano))
    