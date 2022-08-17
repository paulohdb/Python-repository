# enquanto verdade
while True:

    # tentar
    try:
        # sen recebe input
        sen = input()
    
    # Tentativas de eoferror para dar brake
    except EOFError:

        break

    # up recebe true para variação de verificação das
    # letras no booleano
    up = True

    # mess recebe vazio para concatenarmos as letrsa
    mess = ""

    # para i até len de sen - 1
    for i in range(len(sen)):

        car = sen[i]

        if car == " ":

            mess = mess + " "
        
        elif ord(car) >= 65 and ord(car) <= 90:

            if up == True:

                mess = mess + car
            
            else:

                mess = mess + chr(ord(car) + 32)
            
            up = not up

        else:

            if up == True:

                mess = mess + chr(ord(car) - 32)
            
            else:

                mess = mess + car
            
            up = not up

    print(mess)