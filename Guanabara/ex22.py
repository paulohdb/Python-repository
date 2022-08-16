from turtle import st


str_list = input("Digite o seu nome: ").strip()

print("Seu nome com todas as Letras:", str_list.upper())

print("Seu nome com todas as Letras:", str_list.lower())

print("Seu nome com todas as Letras:" .format(len(str_list) - str_list.count(" ")))

sep = str_list.split()

print("Seu primeiro nometem {} letras." .format(sep[0]))