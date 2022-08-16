time = ("Palmeiras", "Athletico-PR", "Atlético-MG", "Corinthians", "Internacinal", "Fluminense", "São Paulo", "Flamengo", "Botafogo", "Santos", "Avaí", "Coritiba", "América-MG", "Bragantino", "Ceará", "Atlético-GO", "Goiás", "Cuiabá", "Juventude", "Fortaleza")

print("Os cinco primeiros da tabela: ")

for i in range(0, 5):

    print(time[i])

print("Os quatro ultimos colocados da tabela: ")

for i in range(16, 20):

    print(time[i])

print("Em ordem alfabética: ")

print(sorted(time))

