def primeira(N: list):

    temp = ""

    for i in range(len(N)):

        car = N[i]

        if car == " ":

            temp = temp + " "
        
        elif ord(car) >= 65 and ord(car) <= 90:

            temp = temp + chr(ord(car) + 3)
        
        elif ord(car) >= 97 and ord(car) <= 122:

            temp = temp + chr(ord(car) + 3)
        
        else:

            temp = temp + car

    return(list(temp))

#====================================================

def segunda(N2: list):

    i = 0
    j = len(N2) - 1

    while i < j:

        temp = N2[i]
        N2[i] = N2[j]
        N2[j] = temp

        i += 1
        j -= 1

#====================================================

def terceira(N3: list):

    tam = len(N3) // 2

    for i in range(tam, len(N3)):

        inv = N3[i]

        N3[i] = chr(ord(inv) - 1)

#====================================================    

def imprime(n: list):

    cripto = ""

    for i in range(len(n)):

        cripto = cripto + n[i]
    
    print(cripto)

#====================================================

def main():

    T = int(input())

    while T > 0:

        li = input()
        
        N = list(li) 

        s1 = primeira(N)

        segunda(s1)

        terceira(s1)

        imprime(s1)

        T -= 1

#========================================

main()