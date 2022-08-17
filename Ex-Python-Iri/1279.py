'''
    Ano Bissexto ou Ano não Bissexto - 1279
    Ler indefinidamente números inteiros
    representando anos, até que EOF seja encontrado.
    Para cada ano lido, deve-se analisar e mostrar
    se o ano é bissexto, huluculu, bulukulu, ou um
    ano comum.
    Para controlar o tipo de ano, serão utilizadas
    variáveis booleanas bissexto, huluculu e bulukulu.
    Entre duas análises completas de um ano deve-se
    mostrar uma linha em branco.
'''

# Whiteline recebe falso
whiteline = False

#enquanto for Verdade:
while True:
    #Tentar
    try:
        #Year recebe um input inteiro
        year = int(input())
    #Se for eoferror
    except EOFError:
        #sair do laço while
        break


    #Atribuir um valor falso para cada situação de leitura de ano!
    bissexto = False
    huluculu = False
    bulukulu = False

    #Se whiteline
    if whiteline:
        #então printar linha branca
        print()
    #Senão
    else:
        #whiteline recebe True
        whiteline = True

    #Se year ter divisão exata por 4 E o ano tiver divisão diferente de 100
    #OU ano for divisivel por 400 exato
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        #então Bissexto recebe True
        bissexto = True
        #Imprimir que é um ano bissexto
        print("This is leap year.")
    #Se year ter divisão exata por 15
    if year % 15 == 0:
        #Então, huluculu recebe True
        huluculu = True
        #Imprimir que é um ano huluculu
        print("This is huluculu festival year.")
    #Se ano ter divisão exata por 55 E for um ano bissexto
    if year % 55 == 0 and bissexto:
        #Então bulukulu recebe True
        bulukulu = True
        #Imprimir que é um ano bulukulu
        print("This is bulukulu festival year.")
    #SE não for bissexto e nao for huluculu e não for bulukulu
    if not bissexto and not huluculu and not bulukulu:
        #Então imprimir que é um ano comum.
        print("This is an ordinary year.")
