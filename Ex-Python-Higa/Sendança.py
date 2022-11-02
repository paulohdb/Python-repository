def converte(lista: list):

    up = True

    sendance = ""

    for i in range(len(lista)):

        car = lista[i]

        if car == " ":

            sendance = sendance + car
        
        #Verifica se carac é maiúsculo
        elif ord(car) >= 65 and ord(car) <= 90:

            if up == True:

                sendance = sendance + car

            else:
                sendance = sendance + chr(ord(car) + 32)

            up = not up
        
        else:
            
            if up == True:

                sendance = sendance + chr(ord(car) - 32)
            
            else:
                
                sendance = sendance + car
            
            up = not up
    
    return sendance

#==============================================

def main():
    while True:
        try:
            sent = list(input())

        except EOFError:
            
            break

        sentence = converte(sent)

        print(sentence)

#==============================================

main()