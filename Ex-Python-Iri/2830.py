
#Duas entradas para os valores dos Mestres
Mk = int(input())
Ml = int(input()) 

#Estrutura lógica: se caso o número dos mestres, subtrair um e dividirmos por 2, e sair o mesmo resultado, irão se enfrentar logo nas oitavas!!
#Exemplo: 1 e 2: ((1-1)/2 = 0), ((2-1)/2 = 0), no entanto, terá o confronto logo nas oitavas! 

if ((Ml-1) // 2 == (Mk-1) // 2):
    print("oitavas")

#Para a próxima etapa, temos os números dos mestres, subtrairmos um e dividirmos por 4, trará o mesmo resultado de quatro em quatro vezes!!
#Exemplo: 1 e 3: ((1-1)/ 4 = 0), ((3-1)/ 4 = 0), no entanto, terá o confronto apenas nas quartas!!

elif ((Ml-1) // 4 == (Mk-1) // 4):
    print("quartas")

elif ((Ml-1) // 8 == (Mk-1) // 8):
    print("semifinal")

else:
    print("finais")

#Detalhe importante!! Sem a divisão de parte inteira, o código não funcionaria pelo fato de não sairem os números inteiros para verificação de equidade dos if's!!