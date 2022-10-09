
def contaLed(lista: list):
    led = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    cont = 0

    for i in range(0, len(lista)):

        ind = 0

        for j in range(0, len(led)):
        
            if lista[i] == ind:

                cont += led[j]
            
            ind += 1
    
    return cont

#==============================================

def main():

    N = int(input())

    while N > 0:

        num = list(map(int, input()))

        qtled = contaLed(num)

        print(f"{qtled} leds")

        N -= 1

#==============================================

main()