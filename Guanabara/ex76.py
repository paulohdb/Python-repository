lst = ("UUUUI", 1.50, "CAVALO", 50.24, "Abubulble", 32.45, "Ele gosta", 13.45, "Que isso meu filho", 4.99, "Se acalme", 4.99)

for i in range(0, len(lst)):

    if i % 2 == 0:

        print("{:.<30}" .format(lst[i]), end="")
    
    else:

        print("R${:>7.2f}" .format(lst[i]))