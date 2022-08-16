preço = float(input("Preço das compras: R$"))

opt = int(input("Qual a forma de pagamento"))

if opt == 1:

    total = preço - (preço * 0.10)

elif opt == 2:

    total = preço - (preço * 0.05)

elif opt == 3:

    total = preço

    parcela = total / 2

    print("Sua compra será parcelada em 2x de R{}" .format(parcela))

elif opt == 4:

    total = preço + (preço * 20 / 100)

    totalparc = int(input("Quantas parcelas?: "))

    parcela = total / totalparc

    print("Sua compra será parcelada em {}x de R${} com JUROS" .format(totalparc, parcela))

else:
    total = preço
    print("OPÇÃO INVÁLIDA")
print("Sua compra de R${} vai custar R${} no final." .format(preço, total))
