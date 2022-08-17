n = int(input())

rato = 0
coelho = 0
sapo = 0

total = 0

pr = 0
pc = 0
ps = 0


for i in range (n):
    
    valor_str, cobaia = input().split()

    valor = int(valor_str)

    total = total + valor

    if cobaia == "C":
        coelho = coelho + valor

    if cobaia == "R":
        rato = rato + valor
    
    if cobaia == "S":
        sapo = sapo + valor

pc = ((coelho * 100)/total)

pr = ((rato * 100)/total)

ps = ((sapo * 100)/total)


print("Total: {} cobaias" .format(total))
print("Total de coelhos: {}" .format(coelho))
print("Total de ratos: {}" .format(rato))
print("Total de sapos: {}" .format(sapo))
print("Percentual de coelhos: {:.2f} %" .format(float(pc)))
print("Percentual de ratos: {:.2f} %" .format(float(pr)))
print("Percentual de sapos: {:.2f} %" .format(float(ps)))