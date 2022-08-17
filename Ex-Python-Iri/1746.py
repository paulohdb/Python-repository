# -*- coding: utf-8 -*-

#Ler 4 valores de valor float

Pv1, Pv2, Pv3, Tp = input().split()

#Os splits estão para os 3 primeiros serem 

prova1 = float(Pv1)
prova2 = float(Pv2)
prova3 = float(Pv3)
trabalhop = float(Tp)

#Código de auxilio para saber qual dos números são os menores
Mn = prova1

if prova2 < Mn:
    Mn = prova2

if prova3 < Mn:
    Mn = prova3

#Aqui seguirá o Cálculo para Obter a Média anual

MediaAnual = ((prova1 + prova2 + prova3) / 3) * 0.8

#Aqui seguirá o Cálculo para Obter a Média do trabalho

MediaTrabalho = trabalhop * 0.2

#Aqui seguirá o Cálculo para Obter a Média Aproveitamento

Ma = MediaAnual + MediaTrabalho

#Se a nota da média de aproveitamento for maior que 6.0 o aluno está aprovado

if Ma >= 6.0:
    print("MA: {:.1f}" .format(Ma))
    print("Estudante Aprovado(a)")

#Se a nota da média de aproveitamento for menor que 6.0 o aluno estará de exame para fazer a prova optativa

elif Ma < 6.0:

    print("O(A) estudante precisa fazer a prova optativa!")

#Aqui, otp será a nota da prova optativa

    opt = float(input())

#Se a prova1 for igual ao menor valor, irá substituir com a opt, para refazer a média

    if prova1 == Mn:
        MediaAnual2 = ((opt + prova2 + prova3) / 3) * 0.8
        Ma2 = MediaAnual2 + MediaTrabalho    

#Se a prova2 for igual ao menor valor, irá substituir com a opt, para refazer a média

    elif prova2 == Mn:
        MediaAnual2 = ((prova1 + opt + prova3) / 3) * 0.8
        Ma2 = MediaAnual2 + MediaTrabalho

#Se a prova3 for igual ao menor valor, irá substituir com a opt, para refazer a média

    elif prova3 == Mn:
        Mn = prova3
        MediaAnual2 = ((prova1 + prova2 + opt) / 3) * 0.8
        Ma2 = MediaAnual2 + MediaTrabalho

#Logo, se A média final for maior que 6.0, o aluno estará aprovado!!


    if Ma2 >= 6.0:
        print("MA: {:.1f}" .format(Ma2)) 
        print("Estudante aprovado(a)")
    
#Se não, Media final for menor que 6.0, o aluno estará reprovado!!

    else:
        Ma2 < 6.0
        print("MA: {:.1f}" .format(Ma2)) 
        print("Estudante reprovado(a)")
