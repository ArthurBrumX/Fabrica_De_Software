ano = int(input("Digite um ano para verificar se é bissexto: "))

ano_bi = ano % 4

if (ano_bi == 0):
    print("o ano é bissexto!")

else:
    print("O ano não é bissexto!")


