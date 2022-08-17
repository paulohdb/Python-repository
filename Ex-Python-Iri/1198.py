
'''
A entrada contém dois números inteiros em cada linha. 
Estes dois números denotam respectivamente a quantidade de soldados do exército de Hashmat e do seu oponente.  
Nenhum número de entrada é maior do que  232. A entrada termina com fim de arquivo (EOF).
'''
#Enquanto verdade
while True: 
    #função try para o bloco que pode gerar a exceção EOFERROR
    try:    

        values = input()
    #EOFError foi encontrado pelo input
    except EOFError: 
        #Quebra do laço e termina o mesmo
        break 
    
    #Ler dois valores, um dos soldados do guerreiro,
    #o outro de seus oponentes (Splitados)
    soldiersH, soldiersO = values.split()

    #transformar os valores lidos em inteiros.

    #NsH recebe soldiersH
    NsH = int(soldiersH)
    #NsO recebe soldiersO
    NsO = int(soldiersO)

    #Imprimir o valor ABSOLUTO da diferença de NsH e NsO
    print(abs(NsO - NsH))