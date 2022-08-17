    # -*- coding: utf-8 -*-

"""
    Problema 1198 do URI - O Bravo Guerreiro Hashmat
    Entrada:
    A entrada contém dois números inteiros em cada
    linha. Estes dois números denotam respectivamente
    a quantidade de soldados do exército de Hashmat
    e do seu oponente.  Nenhum número de entrada é
    maior do que 2³². A entrada termina com fim
    de arquivo (EOF).
    Saída:
    Para cada linha de entrada imprima a diferença
    entre o número de soldados de Hashmat e do seu
    oponente. Cada saída deve ser impressa em uma
    linha separada.    
"""

"""
    Em Python, diferente de linguagens como C e C++, o int
    tem precisão "infinita" (nomenclatura da documentação
    Python 3). Esse termo "infinita" significa que o
    número inteiro pode ser indefinidamente grande.
    Portanto, em Python não precisa se preocupar com o 2³².
    Em Python, quando não há mais entradas a serem lidas
    pelo input(), ou seja, se chegou ao final de arquivo
    (EOF), ele gera uma exceção chamada de EOFError.
    Uma exceção é, basicamente, um sinal de que indica
    que algo não saiu como o esperado.
    A construção para perceber alguma exceção para esse
    problema 1198 é:
    try:    # Inicia uma estrutura que percebe a ocorrência de exceções
            # Indente e coloque a sentença que pode gerar a exceção EOFError
    except EOFError:   # Indica que o bloco de instruções a seguir irá tomar
                       # alguma ação quando a exceção EOFError ocorrer
            # Indente e coloque o que você fará quando EOFError ocorrer
"""
while True: # Continua a repetir o bloco de instruções
            # a seguir até que o break seja executado
    try:    # Inicia o bloco que irá englobar
            # a sentença que pode gerar a exceção EOFError
        valores = input()
    except EOFError: # O EOF foi encontrado por input()
        break # Sai do while e termina o programa
    '''
    Ao testar fora do URI, utilize CTRL-D para simular o
    EOF. Se isso não funcionar, coloque a estrutura if
    comentada a seguir é quando apenas a tecla ENTER
    for digitada na entrada
    if valores == "":
        break
    '''
    sH, so = valores.split()
    nsH = int(sH)
    nso = int(so)
    # O abs() retorna o valor absoluto do número passado
    # como parâmetro e é necessário porque supera a
    # pegadinha que existe entre a ordem de entrada
    # da quantidade de soldados na entrada e a ordem
    # que os dois valores são subtraídos na saída
    # do problema.
    print(abs(nso - nsH))
    """
    dif = nso - nsH
    if dif < 0:
        print(-dif)
    else:
        print(dif)
    """
