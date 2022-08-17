'''
Nesse problema, o código precisará de ler 3 valores str, na qual definirá o tipo de animal
possível com o esquema fornecido no exercicio! da esquerda para a direita!. Ao final dele, terá
o retorno apenas de uma palavra!
'''

#Ler 3 valores para conseguir comparar as str para chegar a qual animal
#o código retornará.
x1 = input()
x2 = input()
x3 = input()

#Como os input's automaticamente são str, não houve necessidade para transformar em str!

#Se x1 igual "vertebrado", prosseguir para o outro se dentro dele
if x1 == "vertebrado":
    #Se x2 igual "ave", prosseguir para o outro se dentro dele
    if x2 == "ave":
        #Se x3 igual carnivoro, print animal "aguia"
        if x3 == "carnivoro":
            #imprimir "aguia" se obedecer todos os if's anteriores
            print("aguia")
        #Se x3 não for igual "carnivoro"
        else:
            #Se x3 igual "onivoro", print animal "pomba"
            if x3 == "onivoro":
                #imprimir "pomba", se o if for obedecido.
                print("pomba")

#Se x1 igual "vertebrado", prosseguir para o outro se dentro dele
if x1 == "vertebrado":
    #Se x2 igual "mamifero", agora será uma outra vertente do esquema do
    #exercício, então, prosseguirá o mesmo caminho que o if anterior de "vertebrado",
    #porém com outras condições
    if x2 == "mamifero":
        #Se x3 igual onivoro, print animal "homem"
        if x3 == "onivoro":
            #imprimir "homem" se obedecer todos os if's anteriores
            print("homem")
        #Se x3 não for igual "onivoro"
        else:
            #Se x3 igual "herbivoro", print animal "vaca"
            if x3 == "herbivoro":
                #imprimir "vaca", se o if for obedecido.
                print("vaca")

#Se x1 igual "invertebrado", prosseguir para o outro se dentro dele
if x1 == "invertebrado":
    #Se x2 igual "inseto", prosseguir para o outro se dentro dele
    if x2 == "inseto":
        #Se x3 igual "hematofago", print animal "pulga"
        if x3 == "hematofago":
            #imprimir "pulga", se o if for obedecido.
            print("pulga")
        #Se x3 não for igual "hematofogo"
        else:
            #Se x3 igual "herbivoro", print animal "lagarta"
            if x3 == "herbivoro":
                #imprimir "lagarta", se o if for obedecido.
                print("lagarta")

#Se x1 igual "invertebrado", prosseguir para o outro se dentro dele
if x1 == "invertebrado":
    #Se x2 igual "anelideo", agora será uma outra vertente do esquema do
    #exercício, então, prosseguirá o mesmo caminho que o if anterior de "invertebrado",
    #porém com outras condições!
    if x2 == "anelideo":
        #Se x3 igual "hematofago", print animal "sanguessuga"
        if x3 == "hematofago":
             #imprimir "sanguessuga", se o if for obedecido.
            print("sanguessuga")
        #Se x3 não for igual "hematofogo"
        else:
            #Se x3 igual "onivoro", print animal "minhoca"
            if x3 == "onivoro":
                 #imprimir "sanguessuga", se o if for obedecido.
                print("minhoca")