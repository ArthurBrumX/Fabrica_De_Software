valor = float(input("Qual o valor do produto: "))

metodo = input("Qual a forma de pagamento: ")

if (metodo == "pix"):

    ajuste = (valor * 10) / 100
    total = valor - ajuste

    print("Para a forma de pagamento pix terá o desconto de 10%")
    print ("o novo valor a ser pago será de: {}".format(total))

elif (metodo == "cartao de credito"):

    pergunta = input ("Vai ser avista ou parcelado: ")

    if (pergunta == "A vista") or (pergunta == "a vista") or (pergunta == "avista") or (pergunta == "Avista"):

        ajuste = (metodo * 5) / 100
        total = valor - ajuste

        print("Para a forma de pagamento cartao de credito terá o desconto de 5%")
        print ("o novo valor a ser pago será de: {}".format(total))
        

    elif (pergunta == "Parcelado") or (pergunta == "parcelado"):

        parcela = input("vai ser parcelada em quatas vezes: ")

        if (parcela == "2x") or (parcela == " 2 vezes"):

            print("Para a forma de pagamento a vista no cartao de credito terá o valor da etiqueta sem juros!")
            print ("o valor a ser pago será de: {}".format(valor))

        elif (parcela == "3x") or (parcela == "3 vezes"):

            ajuste = (metodo * 10) / 100
            total = valor - ajuste

            print("Para a forma de pagamento cartao de credito terá o desconto de 10%")
            print ("o novo valor a ser pago será de: {}".format(total))
