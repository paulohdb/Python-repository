'''
    Inicialmente teremos um laço while, já que foi exposto no exercicio que
    não conterá um input de contagem de caso de testes.

    Então, consequentemente, teremos de ter um try except EOFError, para caso de testes em while.

    Logo depois disso, começaremos com a lógica do problema, terá uma variavel booleana,
    com declaração verdadeira para letras maiusculas com o nome "up". Uma variavel de string
    vazia, para armazenar a sentença dançante.

    Um for i até o tamanho da entrada - 1, para lermos letra por letra.
    car receberá o valor da entrada[i].

    Se car for igual a um espaço, apenas acrescentaremos os espaços dados no input.

    Senão se, nessa condição iremos verificar se o a letra é maiúscula. Utilizando 
    o ord para verificar, na tabela asci, de 65 ao 90, são todas as letras do alfabeto em
    MAIÚSCULO. 
    
    Dentro desse elif iremos verificar se up é verdadeiro, se sim, concatenamos para a variavel
    de string vazia. Se não, concatenaremos com a letra minuscula, somando 32

    senão, se up for verdadeiro, concatenamos danca com a letra maiuscula, subtraindo 32, senão,
    apenas concatenamos danca. up recebe not up

    por fim, printar a mensagem.

'''

# Enquanto verdadeiro
while True:
    # tyr except
    try:

        # sen recebe input
        sen = input()

    # EOFError
    except EOFError:
        # Sair do código
        break

    # up recebe valor Verdadeiro
    up = True

    # variaval dança com string vazia para concatenação
    danca = ""

    # para i até len de sen - 1
    for i in range(len(sen)):

        # car recebe sen[i]
        car = sen[i]

        # se car for igual à um espaço vazio
        if car == " ":

            # danca recebe danca mais um espaço, concatenando assim
            # os espaços existentes no input.
            danca = danca + " "
        
        # Senão se fazer a verificação se a letra é maiúscula
        # com a função ord, utilizando o número decimal.
        elif ord(car) >= 65 and ord(car) <= 90: # Verificar se é Maiúsculo

            # se up igual a verdadeiro
            if up == True:

                # danca recebe danca mais car (concatenação)
                danca = danca + car

            # senão,
            else:
                
                # dança recebe dança mais o caracter minúsculo.
                danca = danca + chr(ord(car) + 32)

            # up recebe not up
            up = not up
        
        #senão
        else:

            # se up for igual a verdadeiro
            if up == True:
                
                # dança recebe dança mais o caracter maiúsculo.
                danca = danca + chr(ord(car) - 32)
            
            #senão
            else:
                
                # danca recebe danca mais car
                danca = danca + car
            
            # up recebe not up
            up = not up

    #mostrar danca
    print(danca)