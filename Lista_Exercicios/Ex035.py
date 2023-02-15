# 35 - O HipermercadoTabajara está com uma promoção decarnes que é imperdível.Confira:

                  # Até 5 Kg              Acima de 5 Kg

# File Duplo      R$ 34,90 por Kg         R$ 35,80 por Kg
# Alcatra         R$ 44,90 por Kg         R$ 46,80 por Kg
# Picanha         R$ 66,90 por Kg         R$ 67,80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,porém não há limites para a quantidade de carne por cliente. 
# Se compra for feita no cartão Tabajara o clientereceberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne 
# comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 

# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.


tipo_carne = input("Qual tipo de carne voce irá querer: ")

# =====================================================================================================================================

if (tipo_carne == "Filé Duplo") or (tipo_carne == "filé Duplo") or (tipo_carne == "file duplo") or (tipo_carne == "File Duplo"):

    kg = float(input("Quantos kilos irá querer: "))

    if (kg <= 5):

        peso = kg * 34.90

        cartao = input("A compra será feita através do cartao da loja [S/N]: ")

        if (cartao == "Sim") or (cartao == "sim") or (cartao == "s") or (cartao == "S"):

            desconto = peso * 5 / 100

            print ("O Valor Final a Ser Pago Será De: R${} ".format(desconto))

        elif (cartao == "Não") or (cartao == "nao") or (cartao == "não") or (cartao == "Nao"):

            print ("O Valor Final a Ser Pago é De: R${}".format(peso))

    # ===========================================================================================

    elif (kg > 5):

        peso = kg * 35.80

        cartao = input("A compra será feita através do cartao da loja [S/N]")

        if (cartao == "Sim") or (cartao == "sim") or (cartao == "s") or (cartao == "S"):

            desconto = peso * 5 / 100

            print ("O valor FInal é de: R${} ".format(desconto))
            
        elif (cartao == "Não") or (cartao == "nao") or (cartao == "não") or (cartao == "Nao"):

            print ("O valor Final é De: R${} ".format(peso))

# ========================================================================================================================================

elif (tipo_carne == "Alcatra") or (tipo_carne == "alcatra") or (tipo_carne == "ALCATRA"):

    kg = float(input("Quantos kilos irá querer: "))

    if (kg <= 5):

        peso = kg * 44.90

        cartao = input("A compra será feita através do cartao da loja [S/N]")

        if (cartao == "Sim") or (cartao == "sim") or (cartao == "s") or (cartao == "S"):

            desconto = peso * 5 / 100

            print ("O valor FInal é de: R${} ".format(desconto))

        elif (cartao == "Não") or (cartao == "nao") or (cartao == "não") or (cartao == "Nao"):

            print ("O valor Final é De: R${} ".format(peso))

    # ===========================================================================================

    elif (kg > 5):

        peso = kg * 46.80

        cartao = input("A compra será feita através do cartao da loja [S/N]")

        if (cartao == "Sim") or (cartao == "sim") or (cartao == "s") or (cartao == "S"):

            desconto = peso * 5 / 100

            print ("O valor FInal é de: R${} ".format(desconto))

        elif (cartao == "Não") or (cartao == "nao") or (cartao == "não") or (cartao == "Nao"):

            print ("O valor Final é De: R${} ".format(peso))

# ========================================================================================================================================

elif (tipo_carne == "Picanha") or (tipo_carne == "picanha") or (tipo_carne == "PICANHA"):

    kg = float(input("Quantos kilos irá querer: "))

    if (kg <= 5):

        peso = kg * 66.90

        cartao = input("A compra será feita através do cartao da loja [S/N]: ")

        if (cartao == "Sim") or (cartao == "sim") or (cartao == "s") or (cartao == "S"):

            desconto = peso * 5 / 100

            print ("O valor FInal é de: R${} ".format(desconto))

        elif (cartao == "Não") or (cartao == "nao") or (cartao == "não") or (cartao == "Nao"):

            print ("O valor Final é De: R${} ".format(peso))

    # ===========================================================================================

    elif (kg > 5):

        peso = kg * 67.80

        cartao = input("A compra será feita através do cartao da loja [S/N]")

        if (cartao == "Sim") or (cartao == "sim") or (cartao == "s") or (cartao == "S"):

            desconto = peso * 5 / 100

            print ("O valor FInal é de: R${} ".format(desconto))

        elif (cartao == "Não") or (cartao == "nao") or (cartao == "não") or (cartao == "Nao"):

            print ("O valor Final é De: R${} ".format(peso))

# ========================================================================================================================================